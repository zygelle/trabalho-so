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

    def tem_fila(self) -> bool:
        return (
            self.fila0
            or self.fila1
            or self.fila2
            or self.bloqueado_memoria
            or self.bloqueado_disco
        )

    def adiciona_processo(self, processos: list[Processo], recursos: Recursos) -> None:
        for processo in processos:
            if processo.aloca(recursos):
                self.fila0.append(processo)
                self.proxFila1.append(processo.numero_processo)
            else:
                self.bloqueado_memoria.append(processo)

    def para_processo(self, processo: Processo, recursos: Recursos) -> None:
        processo.bloqueia(recursos)
        if processo.numero_processo in self.proxFila1:
            self.proxFila1.remove(processo.numero_processo)
            self.fila1.append(processo)
            self.proxFila2.append(processo.numero_processo)
        elif processo.numero_processo in self.proxFila2:
            self.proxFila2.remove(processo.numero_processo)
            self.fila2.append(processo)
        else:
            self.fila0.append(processo)
            self.proxFila1.append(processo.numero_processo)

    def bloqueia_processo_memoria(self, processo: Processo) -> None:
        self.bloqueado_memoria.append(processo)

    def bloqueia_processo_disco(self, processo: Processo) -> None:
        self.bloqueado_disco.append(processo)

    def insere_na_fila_certa(
        self, fila: list[Processo], recursos: Recursos, momento_atual: int
    ) -> None:
        if recursos.checa_possibilidade_aloca_disco(fila[0]):
            processo = fila.pop(0)
            processo.executa(recursos)
            processo.inicio_execucao = momento_atual
            recursos.executando.append(processo)
        else:
            self.bloqueia_processo_disco(fila.pop(0))

    def checa_bloqueados(self, recursos: Recursos):
        pass

    def processa(
        self, recursos: Recursos, momento_atual: int, qtd_processos: int
    ) -> None:
        if len(self.fila0) == 0 and len(self.fila1) == 0 and len(self.fila2) == 0:
            return

        if recursos.cpus > 0:
            for _ in range(recursos.cpus):
                if len(self.fila0) > 0:
                    self.insere_na_fila_certa(self.fila0, recursos, momento_atual)
                elif len(self.fila1) > 0:
                    self.insere_na_fila_certa(self.fila1, recursos, momento_atual)
                elif len(self.fila2) > 0:
                    self.insere_na_fila_certa(self.fila2, recursos, momento_atual)
        else:
            p1: list[Processo] = []
            for i in range(recursos.max_cpus):
                atual_exec = recursos.executando[i]
                if atual_exec.prioridade == 1:
                    p1.append(atual_exec)

            for i in range(
                qtd_processos + len(self.fila0) + len(self.fila1) + len(self.fila2)
            ):
                if i < recursos.cpus:
                    processo = p1[i]
                    if momento_atual > processo.inicio_execucao + self.quantum:
                        self.para_processo(processo, recursos)
                        recursos.executando.remove(processo)
                        if len(self.fila0) > 0:
                            self.insere_na_fila_certa(self.fila0, recursos, momento_atual)
                        elif len(self.fila1) > 0:
                            self.insere_na_fila_certa(self.fila1, recursos, momento_atual)
                        elif len(self.fila2) > 0:
                            self.insere_na_fila_certa(self.fila2, recursos, momento_atual)
