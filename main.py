import streamlit as st
import optimization_hw
import optimization_selflearning
import optimization_vision
import optimization_energy
import optimization_memory

st.set_page_config(page_title="로봇 최적화 시뮬레이터", layout="wide")

st.sidebar.title("🤖 최적화 항목 선택")
page = st.sidebar.radio("탐색할 최적화 분야", [
    "1. 물리적 하드웨어",
    "2. 자체 학습 AI 시스템",
    "3. 비전 시스템",
    "4. 에너지 최적화",
    "5. 메모리 최적화"
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

