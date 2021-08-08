from dataclasses import dataclass
from .Processo import Processo


@dataclass
class Feedback:
    fila0: list[Processo]
    fila1: list[Processo]
    fila2: list[Processo]
    bloqueado_memoria: list[Processo]
    bloqueado_disco: list[Processo]
