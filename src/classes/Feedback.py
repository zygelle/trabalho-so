from dataclasses import dataclass
from .Processo import Processo

@dataclass
class Feedback:
    fila0: list[Processo]
    fila1: list[Processo]
    fila2: list[Processo]
    bloqueadoDisco: list[Processo]
    bloqueadoMemoria: list[Processo]