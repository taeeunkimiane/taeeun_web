import streamlit as st

def run():
    st.title("⚡ 에너지 효율화 최적화 기술 - 공동교육과정")
    st.markdown("""
    ## 1) 회생 제동 시스템
    
    - 💡 **개념**: 로봇이 감속하거나 정지할 때, 관절의 운동 에너지를 전기 에너지로 역변환하여 저장하는 시스템입니다. 이는 전기차에 쓰이는 회생 제동과 원리가 동일합니다.

    - ⚙️ **원리**: BLDC 모터는 역방향으로 회전할 경우 발전기 역할을 하며, 감속 시 **역기전력(Back-EMF)**을 생성 → 브리지 회로를 통해 전류를 저장 장치로 유도합니다.

    - 🔧 **BLDC 모터**: 3상 전류로 회전하며 로터는 영구자석, 스테이터는 코일로 구성. 패러데이 법칙에 따라 강제 회전 시 유도 전류 발생.

    - 🔁 **역기전력과 회로 경로**:
        - Back-EMF는 브리지 회로(H-브리지, 동기 정류기)를 통해 커패시터 또는 배터리로 전달
        - H-브리지는 4개의 MOSFET 또는 IGBT로 구성됨

    - 🔄 **동작 흐름 예시**:
        1. 로봇 감속 → 로터 회전 유지
        2. Back-EMF 발생
        3. 컨트롤러가 회생 모드 전환
        4. 전류가 저장 장치로 흐르며 충전

    ### 🔧 시뮬레이션 예시 (Python)
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    mass = 5.0; v0 = 1.5; eta = 0.7
    time = np.linspace(0, 0.8, 100)
    velocity = v0 * (1 - time / time[-1])
    kinetic_energy = 0.5 * mass * velocity**2
    regenerated_energy = kinetic_energy * eta
    ```

    - 📈 **해석**: 운동 에너지가 시간에 따라 감소하고, 그 중 일부가 회수되어 저장됨

    - 📌 **확장 아이디어**:
        - 다양한 동작 시나리오(걷기, 점프, 착지)별 회수량 비교
        - 슈퍼커패시터 충전 모델 연동
        - STM32 기반 실험 구현 가능
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    ## 2) 피에조 기반 에너지 하베스팅

    - 💡 **개념**: 피에조(Piezoelectric) 소재는 진동, 충격, 압력을 받을 때 전압을 생성. 로봇 움직임에서 발생하는 미세한 힘을 전기 에너지로 변환.

    - ⚙️ **원리**: 피에조 세라믹(PZT, ZnO)은 정압전 효과 → 압력 받으면 전기 신호 출력 → 정류회로 → 축전 장치로 전송

    - 🔧 **구성 요소**: PVDF/PZT 필름, 정류회로, 슈퍼커패시터/미니배터리

    - 📍 **적용 예시**: 발바닥, 무릎, 손가락 등 진동 부위에 설치하여 걷기만으로도 전력 생성 가능
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    ## 3) 스핀트로닉스 기반 저전력 회로

    - 💡 **개념**: 전자의 전하가 아닌 **스핀(spin)**을 사용해 정보를 저장·처리. 스핀 상태(↑, ↓)를 0과 1로 사용.

    - ⚛️ **스핀 원리**: 전자는 스핀이라는 자기 성질을 가지며, 자성체 내부에서 스핀 방향을 이용해 신호 전달 가능

    - 🧩 **핵심 기술**:
        1. **MTJ (Magnetic Tunnel Junction)**: 스핀 정렬이 같으면 낮은 저항 → 0/1 판별
        2. **STT (Spin Transfer Torque)**: 전류에 포함된 스핀이 자성층을 전환시켜 메모리 상태 변경

    - 🔧 **적용 회로**:
        - STT-MRAM: DRAM보다 빠르고, 발열 적고, 비휘발성
        - 스핀 필터 센서: 각도, 회전 정밀 측정 가능

    - 🔋 **효과**: 발열 감소, 에너지 누수 최소화, 재부팅 시 빠른 상태 복구
    """, unsafe_allow_html=True)

    st.markdown("""
    ---
    ## 4) SoC 기반 전력 분산 제어

    - 💡 **개념**: 연산 모듈, 메모리, 센서 I/F를 하나의 칩에 통합하여 전력 소비와 처리 지연을 줄이는 구조

    - 🧠 **원리 및 구조**:
        - CPU + GPU + NPU + 인터페이스 + PMIC 통합
        - DVFS(Dynamic Voltage & Frequency Scaling)로 상황별 전력 분배

    - 🔧 **구성 요소와 반도체 예시**:
        | 구성 요소 | 적용 반도체 |
        |------------|-----------------------------|
        | 연산 처리 | ARM Cortex-A, RISC-V |
        | 신경망 처리 | NPU (Google Edge TPU 등) |
        | 통합 메모리 | LPDDR + STT-MRAM |
        | 센서 I/F | I2C, SPI, ADC, DSP 포함 |
        | 전력 제어 | DVFS + PMIC |

    - 📍 **실사용 예시**:
        - NVIDIA Jetson Nano, Xavier
        - Qualcomm Robotics RB5

    - 🔋 **기대 효과**:
        - 전력 절감, 경량화, 반응성 향상, AI 온디바이스 학습 환경 구성 가능
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ✅ 요약: 에너지 효율화 기술별 정리")
    st.table({
        "기술 항목": ["회생 제동 시스템", "피에조 하베스팅", "스핀트로닉스 회로", "SoC 전력 제어"],
        "핵심 효과": [
            "감속 시 에너지 회수 및 저장",
            "진동/압력 기반 미세 전력 생성",
            "저발열, 비휘발성 고속 메모리",
            "통합 연산 구조로 전력 자율화"
        ]
    })

    st.markdown("---")
    st.caption("📁 optimization_energy_extended.py | 로봇 에너지 효율 최적화 구성 전체 페이지")
