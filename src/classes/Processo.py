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

    def termina(self, recursos: Recursos):
        recursos._libera_disco(self.unidade_disco)
        recursos._libera_memoria(self.memoria)
        recursos._libera_cpu()
    
    def executa(self, recurso: Recursos) -> bool:
        if not recurso.aloca_cpu():
            return False
        if not recurso.aloca_disco(self.unidade_disco):
            recurso._libera_cpu()
            return False
        return True   

    def aloca(self, recurso: Recursos) -> bool:
        if not recurso.aloca_memoria(self.memoria):
            return False
        return True

    def bloqueia(self, recursos: Recursos):
        recursos._libera_cpu()
        recursos._libera_disco(self.unidade_disco)

    def libera(self, recursos: Recursos):
        recursos._libera_memoria(self.memoria)