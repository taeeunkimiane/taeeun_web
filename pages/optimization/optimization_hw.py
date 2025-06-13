import streamlit as st

def run():
    st.title("🚀 로봇 최적화 효과 예측 시뮬레이터")

    st.sidebar.header("🧪 예측 항목 선택")
    section = st.sidebar.radio(
        "예측할 최적화 영역을 선택하세요:",
        [
            "1. 물리적 구성 요소",
            "2. 센서 및 처리 시스템",
            "3. 처리 하드웨어 및 통신",
            "4. 시뮬레이션 및 트윈"
        ]
    )

    if section == "1. 물리적 구성 요소":
        st.header("① 물리적 구성 요소 선택")
        material = st.selectbox("재료 선택", ["탄소섬유 복합재료 (CFRP)", "마그네슘 합금", "알루미늄 합금 (7075, 6061)"])
        structure = st.selectbox("구조 선택", ["벌집 구조(Honeycomb via FEA)", "위상 최적화 (Topology Optimization)", "중공 구조 (Hollow Arm)"])
        analysis = st.selectbox("해석 사용 유무", ["사용 (ANSYS / Abaqus)", "미사용"])
        if st.button("①번 예측 실행"):
            show_effects_for_1(material, structure, analysis)

    elif section == "2. 센서 및 처리 시스템":
        st.header("② 센서 및 처리 시스템 선택")
        sensors = []
        if st.checkbox("센서: LiDAR"): sensors.append("LiDAR")
        if st.checkbox("센서: IMU"): sensors.append("IMU")
        if st.checkbox("센서: Thermal 카메라"): sensors.append("Thermal 카메라")
        onboard = st.selectbox("엣지 처리 방식", ["온보드 처리 (엣지 프로세싱)", "외부 처리"])
        size = st.selectbox("자원 고려 요소", ["전력", "크기", "열"])
        processing = st.selectbox("엣지 프로세서", ["NVIDIA GPU", "TPU", "ARM CPU"])
        if st.button("②번 예측 실행"):
            show_effects_for_2(sensors, onboard, size, processing)

    elif section == "3. 처리 하드웨어 및 통신":
        st.header("③ 하드웨어 플랫폼 선택")
        sbc = st.selectbox("SBC 선택", ["Jetson Xavier NX", "Raspberry Pi 4"])
        ai_hw = st.selectbox("AI 하드웨어 선택", ["TPU (Google Coral)", "FPGA (Intel/Xilinx)"])
        comm = st.multiselect("통신 방식 선택", ["ROS 2.0 DDS", "CAN"])
        if st.button("③번 예측 실행"):
            show_effects_for_3(sbc, ai_hw, comm)

    elif section == "4. 시뮬레이션 및 트윈":
        st.header("④ 시뮬레이션 환경 설정")
        twin = st.checkbox("디지털 트윈 적용", value=True)
        simulator = st.selectbox("시뮬레이터", ["Gazebo", "CoppeliaSim (구 V-REP)", "Webots", "Unity 기반 시뮬레이터"])
        motion = st.checkbox("동작 시뮬레이션 포함", value=True)
        sensor_sim = st.checkbox("센서 시뮬레이션 포함", value=True)
        if st.button("④번 예측 실행"):
            show_effects_for_7(twin, simulator, motion, sensor_sim)

def show_effects_for_1(material, structure, analysis):
    st.subheader("📊 [1] 물리적 구성 요소 최적화 효과")
    if material == "탄소섬유 복합재료 (CFRP)":
        st.info("📉 무게 -45% / 📈 강성 유지 80~90% / ⚠️ 고가, 가공 어려움")
    elif material == "마그네슘 합금":
        st.info("📉 무게 -35% / ⚠️ 부식성, 충격 약함 / 🧪 열처리·코팅 필요")
    elif material == "알루미늄 합금 (7075, 6061)":
        st.info("⚖️ 무게-강도 절충 / 💰 비용 효율 우수 / 🔁 범용성 높음")

    if structure == "벌집 구조(Honeycomb via FEA)":
        st.success("🧠 하중 분산 최적화 / 📈 강성 +30% 증가")
    elif structure == "위상 최적화 (Topology Optimization)":
        st.success("🎯 재료 효율성 ↑ / 📉 사용량 -20% / 📈 강성 대비 무게비 ↑")
    elif structure == "중공 구조 (Hollow Arm)":
        st.success("🔩 중량 절감 구조 / ⚠️ 진동 억제 및 보강 설계 필요")

    if analysis == "사용 (ANSYS / Abaqus)":
        st.info("🔍 정밀 해석 가능 → 응력/변형률 분석으로 설계 신뢰도 향상")
    else:
        st.warning("❗ 해석 미사용 시 설계 오차 증가 가능성 있음")

def show_effects_for_2(sensors, onboard, size, processing):
    st.subheader("📊 [2] 센서 및 처리 시스템 효과")
    if "LiDAR" in sensors:
        st.info("🌐 고정밀 3D 인식 → 충돌 회피 및 거리 계산 정밀도 ↑")
    if "IMU" in sensors:
        st.info("🎯 자세 보정 가능 → 동적 안정성 향상")
    if "Thermal 카메라" in sensors:
        st.info("🌡️ 온도 감지 → 화재, 생명체 반응 탐지에 유리")

    if onboard == "온보드 처리 (엣지 프로세싱)":
        st.success("⚡ 실시간 반응 가능 / 지연 최소화 / 통신 의존도 낮음")
    else:
        st.warning("🌐 통신망 의존 / 실시간성 제한 우려")

    if size == "전력":
        st.info("🔋 저전력 설계 중요 → 배터리 지속시간에 직접 영향")

    st.info(f"✅ '{processing}'는 엣지 추론에 최적화된 하드웨어입니다.")

def show_effects_for_3(sbc, ai_hw, comm):
    st.subheader("📊 [3] 처리 하드웨어 및 통신 효과")
    if sbc == "Jetson Xavier NX":
        st.success("🚀 AI 추론 가능 (최대 21TOPS) → 고성능 엣지 컴퓨팅")
    elif sbc == "Raspberry Pi 4":
        st.info("💡 저전력 범용 SBC → 고성능 AI에는 제약 있음")

    if ai_hw == "TPU (Google Coral)":
        st.info("⚡ 4TOPS+ 처리 / 모바일 AI 추론에 최적")
    elif ai_hw == "FPGA (Intel/Xilinx)":
        st.info("🔧 맞춤 회로 구성 → 알고리즘 유연성 + 저전력")

    if "ROS 2.0 DDS" in comm:
        st.success("🧠 고속 분산 통신 구조 → 실시간 로봇 제어에 적합")
    if "CAN" in comm:
        st.info("🚗 안정적인 산업용 통신 → 오류 내성 우수")

def show_effects_for_7(twin, simulator, motion, sensor_sim):
    st.subheader("📊 [4] 시뮬레이션 및 트윈 효과")
    if twin:
        st.success("🧠 디지털 트윈 적용 → 가상-현실 연동, 고장 예측 가능")

    if simulator == "Gazebo":
        st.info("🛰️ ROS 기반 로봇 시뮬레이션에 널리 사용되는 시뮬레이터")
    elif simulator == "CoppeliaSim (구 V-REP)":
        st.info("🤖 GUI 편리 / 플러그인 확장성 우수")
    elif simulator == "Webots":
        st.info("🌐 빠른 실행 / 센서 시각화 우수")
    elif simulator == "Unity 기반 시뮬레이터":
        st.info("🎮 시각적 표현 탁월 / 디지털 트윈 시각화 유리")

    if motion:
        st.success("🛣️ 동작 시뮬레이션 포함 → 경로 계획, 충돌 회피 알고리즘 검증 가능")

    if sensor_sim:
        st.success("📷 센서 시뮬레이션 포함 → 데이터 정밀도/해석 성능 검증 가능")
        st.info("🔍 다양한 환경에서 센서 테스트 가능")
