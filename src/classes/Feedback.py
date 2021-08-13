from dataclasses import dataclass, field
from .Processo import Processo
from .Recursos import Recursos

@dataclass(init=True)
class Feedback:
    fila0: list[Processo] = field(default_factory=list)
    fila1: list[Processo] = field(default_factory=list)
    fila2: list[Processo] = field(default_factory=list)
    bloqueado_memoria: list[Processo] = field(default_factory=list)
    bloqueado_disco: list[Processo] = field(default_factory=list)
    proxFila1: list[int] = field(default_factory=list)
    proxFila2: list[int] = field(default_factory=list)
    quantum: int = 2

    def adiciona_processo(self, processo: list[Processo], recursos: Recursos) -> None:
        for p in processo:
            if (p.aloca(recursos)):
                self.fila0.append(processo)
                self.proxFila1.append(processo.numero_processo)
            else:
                self.bloqueado_memoria.append(p)
    
    def para_processo(self, processo: Processo, recursos: Recursos) -> None:
        processo.bloqueia(recursos)
        if (processo.numero_processo in self.proxFila1):
            self.fila1.append(processo)
        elif (processo.numero_processo in self.proxFila2):
            self.fila2.append(processo)
        else:
            self.fila0.append(processo)
    
    def bloqueia_processo_memoria(self, processo: Processo) -> None:
        self.bloqueado_memoria.append(processo)
    
    def bloqueia_processo_disco(self, processo: Processo) -> None:
        self.bloqueado_disco.append(processo)

    def processa(recursos: Recursos) -> None:
        pass