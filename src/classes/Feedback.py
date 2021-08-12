from dataclasses import dataclass, field
from .Processo import Processo


@dataclass(init=True)
class Feedback:
    fila0: list[Processo] = field(default_factory=list)
    fila1: list[Processo] = field(default_factory=list)
    fila2: list[Processo] = field(default_factory=list)
    bloqueado_memoria: list[Processo] = field(default_factory=list)
    bloqueado_disco: list[Processo] = field(default_factory=list)

    def adiciona_processo(self, processo: Processo):
        self.fila0.append(processo)
