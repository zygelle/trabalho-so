from dataclasses import dataclass
from typing import Tuple


@dataclass(init=True)
class Recursos:
    cpus: int = 4
    mem: int = 16000
    discos: int = 4

    def alocaMemoria(self, memoria: int) -> bool:
        if self.mem - memoria >= 0:
            self.mem -= memoria
            return True
        return False

    def _liberaMemoria(self, memoria: int):
        self.mem += memoria

    def alocaCPU(self) -> bool:
        if self.cpus > 0:
            self.cpus -= 1
            return True
        return False

    def _liberaCPU(self):
        self.cpus += 1

    def alocaDisco(self, numeroDiscos: int) -> bool:
        if self.discos - numeroDiscos >= 0:
            self.discos -= numeroDiscos
            return True
        return False

    def _liberaDisco(self, numeroDiscos: int):
        self.discos += numeroDiscos
