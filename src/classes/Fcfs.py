from dataclasses import dataclass, field
from classes.Feedback import Feedback

from classes.Recursos import Recursos
from .Processo import Processo


@dataclass(init=True)
class Fcfs:
    fila: list[Processo] = field(default_factory=list)

    def adiciona_processo(self, processo: list[Processo], recursos: Recursos) -> None:
        for p in processo:
            p.aloca(recursos)
            self.fila.append(p)

    def processa(self, recursos: Recursos, feedback: Feedback):
        if not self.fila:
            return

        p1 = []
        if recursos.cpus == 0:
            for i in range(recursos.max_cpus):
                atual_exec = recursos.executando[i]
                if atual_exec.prioridade == 1:
                    p1.append(i)

            for i in p1:
                if not self.fila:
                    return

                self.fila[0].executa(recursos)
                feedback.adiciona_processo(recursos.executando[i])
                recursos.executando[i] = self.fila.pop(0)

        else:
            for _ in range(recursos.max_cpus):
                if not self.fila:
                    return

                self.fila[0].executa(recursos)
                recursos.executando.append(self.fila.pop(0))
