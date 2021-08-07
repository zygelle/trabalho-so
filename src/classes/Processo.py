from dataclasses import dataclass
from .Recursos import Recursos


@dataclass(init=True)
class Processo:
    numero_processo: int
    tempo_de_chegada: int
    prioridade: int
    tempo_de_processador: int
    memoria: int
    unidade_disco: int

    def liberaProcesso(self, recursos: Recursos):
        recursos._liberaDisco(self.unidade_disco)
        recursos._liberaMemoria(self.memoria)
        recursos._liberaCPU()


def alocaProcesso(processo: Processo, recurso: Recursos) -> Processo:
    if not recurso.alocaCPU():
        return None
    if not recurso.alocaDisco(processo.unidade_disco):
        recurso._liberaCPU()
        return None
    if not recurso.alocaMemoria(processo.memoria):
        recurso._liberaCPU()
        recurso._liberaMemoria(processo.unidade_disco)
        return None
    return processo
