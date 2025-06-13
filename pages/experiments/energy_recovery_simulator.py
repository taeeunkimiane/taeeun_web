# experiments/energy_recovery_simulator.py
import streamlit as st
import plotly.graph_objs as go

# 시나리오별 계수 설정 (걷기, 뛰기 등)
ENERGY_COEFFS = {
    "걷기": 0.5,
    "뛰기": 1.2,
    "낙하": 2.5,
    "넘어짐": 1.8,
}

# 기본 질량 (예: 로봇 무게)
ROBOT_MASS = 70  # kg

# 에너지 회수량 계산 함수
def calculate_energy(v, motion_type, piezo=True, regen=True):
    k = ENERGY_COEFFS.get(motion_type, 1.0)
    base_energy = k * ROBOT_MASS * v ** 2  # E = k · m · v²
    piezo_energy = base_energy * 0.3 if piezo else 0
    regen_energy = base_energy * 0.5 if regen else 0
    return piezo_energy + regen_energy

# 시뮬레이터 UI 정의
def app():
    st.title("2️⃣  에너지 회수 시뮬레이터")
    st.markdown("""
    로봇의 동작 방식, 속도, 회로 조합에 따라 회수 가능한 에너지를 시뮬레이션합니다.
    """)

    col1, col2 = st.columns(2)
    with col1:
        motion_type = st.selectbox("동작 형태", list(ENERGY_COEFFS.keys()))
        speed = st.slider("속도 (m/s)", 0.1, 3.0, 1.0, step=0.1)
    with col2:
        use_piezo = st.checkbox("피에조 회로 사용", value=True)
        use_regen = st.checkbox("회생 제동 회로 사용", value=True)

    # 계산
    energy = calculate_energy(speed, motion_type, piezo=use_piezo, regen=use_regen)
    base = calculate_energy(speed, motion_type, piezo=False, regen=False)

    st.subheader("⚡ 회수 가능한 에너지 예측")
    st.metric("총 회수 에너지", f"{energy:.2f} J")

    # 시나리오별 비교 그래프
    st.subheader("📊 동작별 회수 에너지 비교")
    speeds = [i/10 for i in range(1, 31)]
    energy_vals = [calculate_energy(s, motion_type, use_piezo, use_regen) for s in speeds]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=speeds, y=energy_vals, mode='lines+markers', name='회수 에너지'))
    fig.update_layout(xaxis_title="속도 (m/s)", yaxis_title="에너지 (J)", height=400)
    st.plotly_chart(fig)

    # 배터리 지속시간 변화 시뮬레이션
    st.subheader("🔋 배터리 지속시간 변화 예측")
    battery_capacity = 10000  # mAh, 예시값
    voltage = 7.4  # V
    recovered_wh = energy / 3600 * voltage  # J → Wh 변환
    st.write(f"예상 회수 에너지는 약 {recovered_wh:.3f} Wh 로, 배터리 지속시간을 소폭 연장할 수 있습니다.")
