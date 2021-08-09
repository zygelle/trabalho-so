from dataclasses import dataclass
from .Processo import Processo


@dataclass
class Fcfs:
    fila: list[Processo]
