from dataclasses import dataclass, field
from classes.Feedback import Feedback

from classes.Recursos import Recursos
from .Processo import Processo


@dataclass(init=True)
class Fcfs:
    fila: list[Processo] = field(default_factory=list)
    bloqueado_memoria: list[Processo] = field(default_factory=list)

    def adiciona_processo(self, processo: list[Processo], recursos: Recursos, feedback: Feedback) -> None:
        for p in processo:
            while(not p.aloca(recursos)):
                if (len(feedback.fila2) > 0):
                    processo = feedback.fila2.pop(len(feedback.fila2))
                    processo.libera()
                    feedback.bloqueia_processo_memoria(processo)
                elif (len(feedback.fila1) > 0):
                    processo = feedback.fila1.pop(len(feedback.fila1))
                    processo.libera()
                    feedback.bloqueia_processo_memoria(processo)
                elif (len(feedback.fila0) > 0):
                    processo = feedback.fila0.pop(len(feedback.fila0))
                    processo.libera()
                    feedback.bloqueia_processo_memoria(processo)
                else:
                    self.bloqueado_memoria.append(p)
                    break
            if (p not in self.bloqueado_memoria):
                self.fila.append(p)


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
            p1 = []
            for i in range(recursos.max_cpus):
                atual_exec = recursos.executando[i]
                if atual_exec.prioridade == 1:
                    p1.append(i)

            for i in p1:
                if not self.fila:
                    return

                feedback.para_processo(p1)
                recursos.executando.remove(p1)
                self.fila[0].executa(recursos)
                recursos.executando.append(self.fila.pop(0))
