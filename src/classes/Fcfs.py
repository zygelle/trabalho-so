from dataclasses import dataclass, field
from classes.Feedback import Feedback

from classes.Recursos import Recursos
from .Processo import Processo


@dataclass(init=True)
class Fcfs:
    fila: list[Processo] = field(default_factory=list)
    bloqueado_memoria: list[Processo] = field(default_factory=list)

    def tem_fila(self) -> bool:
        return self.fila or self.bloqueado_memoria

    def adiciona_processo(
        self, processo: list[Processo], recursos: Recursos, feedback: Feedback
    ) -> None:
        for p in processo:
            while not p.aloca(recursos):
                if len(feedback.fila2) > 0:
                    processo = feedback.fila2.pop(len(feedback.fila2) - 1)
                    processo.libera(recursos)
                    feedback.bloqueia_processo_memoria(processo)
                elif len(feedback.fila1) > 0:
                    processo = feedback.fila1.pop(len(feedback.fila1) - 1)
                    processo.libera(recursos)
                    feedback.bloqueia_processo_memoria(processo)
                elif len(feedback.fila0) > 0:
                    processo = feedback.fila0.pop(len(feedback.fila0) - 1)
                    processo.libera(recursos)
                    feedback.bloqueia_processo_memoria(processo)
                else:
                    self.bloqueado_memoria.append(p)
                    break
            if p not in self.bloqueado_memoria:
                self.fila.append(p)

    def checa_bloqueados(self, recursos: Recursos, feedback: Feedback):
        if self.bloqueado_memoria:
            for processo in self.bloqueado_memoria:
                if recursos.checa_possibilidade_aloca_memoria(processo):
                    processo.aloca(recursos)
                    self.fila.append(processo)
                    self.bloqueado_memoria.remove(processo)

    def processa(self, recursos: Recursos, feedback: Feedback):
        if not self.fila:
            return

        if recursos.cpus > 0:
            for _ in range(recursos.cpus):
                if not self.fila:
                    return

                self.fila[0].executa(recursos)
                recursos.executando.append(self.fila.pop(0))
        else:
            p1: list[Processo] = []
            for i in range(recursos.max_cpus):
                atual_exec = recursos.executando[i]
                if atual_exec.prioridade == 1:
                    p1.append(atual_exec)

            for processo in p1:
                if not self.fila:
                    return

                feedback.para_processo(processo, recursos)
                recursos.executando.remove(processo)
                self.fila[0].executa(recursos)
                recursos.executando.append(self.fila.pop(0))
