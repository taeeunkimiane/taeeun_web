# optimization/optimization.py 내부

from . import optimization_energy
from . import optimization_hw
from . import optimization_memory
from . import optimization_selflearning
from . import optimization_vision

modules = {
    "1. 물리적 하드웨어": optimization_hw.run,
    "2. 자체 학습 AI 시스템": optimization_selflearning.run,
    "3. 비전 시스템": optimization_vision.run,
    "4. 에너지 최적화": optimization_energy.run,
    "5. 메모리 최적화": optimization_memory.run,
}

def get_module(name: str):
    return modules.get(name, lambda: None)

