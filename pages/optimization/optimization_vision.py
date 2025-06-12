import streamlit as st

def run():
    st.title("👁️ 비전 시스템 최적화")

    st.markdown("""
    ### 🎯 최적화 목표
    - 다양한 환경(조명 변화, 왜곡 등)에서도 **고정밀 시각 정보 인식**과 **실시간 분석**이 가능한 비전 시스템을 구축합니다.
    - 딥러닝 + 전통 컴퓨터 비전 알고리즘의 융합으로 **다층 시각 처리 체계**를 구성합니다.
    """)

    st.markdown("### 🔧 기술 적용")

    with st.expander("1️⃣ YOLOv8-tiny + Depth Camera + OpenPose 융합"):
        st.write("""
        - 🧠 **YOLOv8-tiny**: 경량 객체 탐지 모델 → 빠른 연산 속도 유지하며 객체 감지
        - 📏 **Depth Camera**: 거리 정보를 활용해 2D + 3D 객체 위치 동시 파악
        - 🧍 **OpenPose**: 관절 추정을 통해 사람의 동작 패턴 인식
        - 📦 융합 결과: '어떤 사람이 어디서 어떤 행동을 하는지'까지 실시간 분석 가능
        """)

    with st.expander("2️⃣ SIFT 기반 객체 정합 및 대응점 추출"):
        st.write("""
        - 📌 **SIFT(Scale Invariant Feature Transform)**:
            - 이미지 스케일, 회전 변화에도 강인한 특징점 추출 알고리즘
        - 🔍 영상 속 물체와 저장된 특징점을 매칭하여 **정확한 객체 인식** 가능
        - 🤖 로봇이 동일한 물체를 다양한 환경에서 인식할 수 있도록 함
        """)

    with st.expander("3️⃣ 허프 변환을 통한 경계 및 장애물 인식"):
        st.write("""
        - 📐 직선, 원형 같은 기하학적 경계를 검출하는 데 탁월한 **허프 변환(Hough Transform)** 적용
        - 🧱 벽, 계단, 원통형 장애물 등을 감지 → 자율 주행 또는 동작 경로 판단에 활용
        """)

    with st.expander("4️⃣ 다중 스케일 윤곽선 피라미드 적용"):
        st.write("""
        - 🌀 다양한 해상도에서 이미지 윤곽선을 추출 → 각 레벨별로 특징을 적응적으로 결합
        - 🔍 저해상도에서 대략적 경계, 고해상도에서 세부 경계 분석 가능
        - 📊 Gaussian Pyramid + DoG (Difference of Gaussians) 구조 기반
        """)

    st.markdown("""
    ### ✅ 기대 효과
    - 📹 영상 왜곡, 조명 변화에 강한 인식 능력 확보
    - 🧠 사람의 행동을 3D 기반으로 정확하게 파악
    - 🚧 복잡한 환경에서도 실시간 장애물 감지 및 경로 설정 가능
    """)

    st.markdown("### 🧠 적용 예시")
    col1, col2 = st.columns(2)
    with col1:
        st.info("👣 사람의 관절 추적 + 행동 분류 → 위험 행동 감지 시스템")
    with col2:
        st.info("🚗 Depth 기반 시야 인식 + SIFT + 허프변환 → 실내 자율주행 로봇")

    st.markdown("---")
    st.caption("📁 optimization_vision.py | 복합 시각 인식 시스템 최적화 구성")
