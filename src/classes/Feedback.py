from dataclasses import dataclass
from .Processo import Processo


@dataclass(init=True)
class Feedback:
    fila0: list[Processo]
    fila1: list[Processo]
    fila2: list[Processo]
    bloqueado_memoria: list[Processo]
    bloqueado_disco: list[Processo]

    def adiciona_processo(self, processo: Processo):
        self.fila0.append(processo)
