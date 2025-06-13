import streamlit as st

st.set_page_config(page_title="로봇 최적화 시뮬레이터", layout="wide")

# ✅ pages 폴더 안에서 가져오므로 이렇게 수정
from pages.optimization import optimization_hw
from pages.optimization import optimization_selflearning
from pages.optimization import optimization_vision
from pages.optimization import optimization_energy
from pages.optimization import optimization_memory
from pages.experiments import optim_simulator, energy_recovery_simulator, edge_filter_simulator

st.sidebar.title("🤖 최적화 항목 선택")
page = st.sidebar.radio("탐색할 최적화 분야", [
    "1. 물리적 하드웨어",
    "2. 자체 학습 AI 시스템",
    "3. 비전 시스템",
    "4. 에너지 최적화",
    "5. 메모리 최적화",
    "6. 실험 시뮬레이터"  # ✅ 실험 추가
])

if page == "1. 물리적 하드웨어":
    optimization_hw.run()
elif page == "2. 자체 학습 AI 시스템":
    optimization_selflearning.run()
elif page == "3. 비전 시스템":
    optimization_vision.run()
elif page == "4. 에너지 최적화":
    optimization_energy.run()
elif page == "5. 메모리 최적화":
    optimization_memory.run()
elif page == "6. 실험 시뮬레이터":
    optim_simulator.app()  # ✅ pages/experiments/optim_simulator.py 안의 run()
    energy_recovery_simulator.app()  # ✅ pages/experiments/energy_recovery_simulator.py 안의 run()
    edge_filter_simulator.app()  # ✅ pages/experiments/edge_filter_simulator.py 안의 run()
