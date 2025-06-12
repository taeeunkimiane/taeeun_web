# experiments/edge_filter_simulator.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# 가우시안 필터 함수
def apply_gaussian(img, sigma):
    ksize = int(6 * sigma + 1)
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)

# DoG (Difference of Gaussians)
def apply_dog(img, sigma):
    blur1 = cv2.GaussianBlur(img, (0, 0), sigma)
    blur2 = cv2.GaussianBlur(img, (0, 0), sigma * 1.6)
    dog = cv2.subtract(blur1, blur2)
    return dog

# LoG (Laplacian of Gaussian)
def apply_log(img, sigma):
    blur = cv2.GaussianBlur(img, (0, 0), sigma)
    log = cv2.Laplacian(blur, cv2.CV_64F)
    return np.uint8(np.absolute(log))

# Streamlit 앱 함수
def app():
    st.title("2️⃣ 윤곽선 필터 시뮬레이터")
    st.markdown("""
    업로드한 이미지에 대해 가우시안 필터를 적용하고, DoG/LoG 기반 윤곽선을 시각화합니다.
    """)

    uploaded = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])
    example = st.checkbox("예시 이미지 사용 (Lenna)")
    sigma = st.slider("σ (가우시안 표준편차)", 0.1, 3.0, 1.0, step=0.1)

    if uploaded:
        image = Image.open(uploaded).convert("RGB")
    elif example:
        from skimage import data
        image = Image.fromarray(data.astronaut())
    else:
        st.info("이미지를 업로드하거나 예시를 선택하세요.")
        return

    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    gaussian_img = apply_gaussian(gray, sigma)
    dog_img = apply_dog(gray, sigma)
    log_img = apply_log(gray, sigma)

    st.subheader("🖼️ 필터 결과 비교")
    col1, col2 = st.columns(2)

    with col1:
        st.image(gray, caption="원본 그레이스케일", use_column_width=True)
        st.image(gaussian_img, caption=f"가우시안 필터 적용 (σ={sigma})", use_column_width=True)
    with col2:
        st.image(dog_img, caption=f"DoG (σ={sigma}, σ×1.6)", use_column_width=True)
        st.image(log_img, caption="LoG (Laplacian of Gaussian)", use_column_width=True)

