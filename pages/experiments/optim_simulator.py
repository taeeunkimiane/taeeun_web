# experiments/optim_simulator.py
import streamlit as st
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import plotly.graph_objs as go
import numpy as np

# 간단한 MLP 모델 정의
class SimpleMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = self.relu(self.fc1(x))
        return self.fc2(x)

# 훈련 함수 정의
def train_model(optimizer_name, lr, beta1, beta2, weight_decay, epochs=5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleMLP().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer_dict = {
        "SGD": optim.SGD(model.parameters(), lr=lr, weight_decay=weight_decay),
        "Adam": optim.Adam(model.parameters(), lr=lr, betas=(beta1, beta2), weight_decay=weight_decay),
        "RMSProp": optim.RMSprop(model.parameters(), lr=lr, weight_decay=weight_decay),
        "AdamW": optim.AdamW(model.parameters(), lr=lr, betas=(beta1, beta2), weight_decay=weight_decay),
    }
    optimizer = optimizer_dict[optimizer_name]

    transform = transforms.ToTensor()
    train_data = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    loss_list = []
    acc_list = []
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        model.train()
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        loss_list.append(total_loss / len(train_loader))
        acc_list.append(correct / total)

    return loss_list, acc_list

# Streamlit 앱 함수
def app():
    st.title("1️⃣ 최적화 알고리즘 시뮬레이터")
    st.markdown("""
    PyTorch 기반 MLP 모델을 다양한 옵티마이저로 학습시키고, 손실 및 정확도 그래프를 비교합니다.
    """)

    col1, col2 = st.columns(2)
    with col1:
        optimizer_name = st.selectbox("Optimizer 선택", ["SGD", "Adam", "RMSProp", "AdamW"])
        lr = st.slider("Learning Rate", 0.0001, 0.1, 0.001, step=0.0001)
        beta1 = st.slider("β₁", 0.0, 0.999, 0.9, step=0.01)
        beta2 = st.slider("β₂", 0.0, 0.999, 0.999, step=0.001)
        weight_decay = st.slider("Weight Decay", 0.0, 0.1, 0.01, step=0.001)
    
    start = st.button("학습 시작")
    reset = st.button("리셋")

    if start:
        with st.spinner("모델 학습 중..."):
            loss, acc = train_model(optimizer_name, lr, beta1, beta2, weight_decay)

        epochs = list(range(1, len(loss)+1))

        st.subheader("📉 Loss vs Epoch")
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=epochs, y=loss, mode="lines+markers", name="Loss"))
        fig1.update_layout(xaxis_title="Epoch", yaxis_title="Loss")
        st.plotly_chart(fig1)

        st.subheader("✅ Accuracy vs Epoch")
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=epochs, y=acc, mode="lines+markers", name="Accuracy"))
        fig2.update_layout(xaxis_title="Epoch", yaxis_title="Accuracy")
        st.plotly_chart(fig2)

    if reset:
        st.experimental_rerun()

