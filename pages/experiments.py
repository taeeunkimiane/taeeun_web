# experiments.py (루트)
import streamlit as st
from experiments import optim_simulator, energy_recovery_simulator, edge_filter_simulator
from experiments.optimization import (
    optimization_hw, optimization_energy, optimization_memory,
    optimization_vision, optimization_selflearning
)

def app():
    st.title("🧪 통합 실험 대시보드")
    st.markdown(\"\"\"
    아래 실험 항목 중 하나를 선택하여 결과를 시각화하고 비교해보세요.
    \"\"\")

    option = st.selectbox("🧭 실험 선택", [
        "최적화 알고리즘 시뮬레이터",
        "윤곽선 필터 시뮬레이터",
        "에너지 회수 시뮬레이터",
        "하드웨어 최적화",
        "에너지 최적화",
        "메모리 최적화",
        "비전 최적화",
        "자기지도 학습 최적화"
    ])

    if option == "최적화 알고리즘 시뮬레이터":
        optim_simulator.app()
    elif option == "윤곽선 필터 시뮬레이터":
        edge_filter_simulator.app()
    elif option == "에너지 회수 시뮬레이터":
        energy_recovery_simulator.app()
    elif option == "하드웨어 최적화":
        optimization_hw.app()
    elif option == "에너지 최적화":
        optimization_energy.app()
    elif option == "메모리 최적화":
        optimization_memory.app()
    elif option == "비전 최적화":
        optimization_vision.app()
    elif option == "자기지도 학습 최적화":
        optimization_selflearning.app()

