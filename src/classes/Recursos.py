from dataclasses import dataclass


@dataclass(init=True)
class Recursos:
    executando: list

    cpus: int = 4
    max_cpus: int = cpus
    memoria: int = 16000
    discos: int = 4

    def aloca_memoria(self, memoria: int) -> bool:
        if self.memoria - memoria >= 0:
            self.memoria -= memoria
            return True
        return False

    def _libera_memoria(self, memoria: int):
        self.memoria += memoria

    def aloca_cpu(self) -> bool:
        if self.cpus > 0:
            self.cpus -= 1
            return True
        return False

    def _libera_cpu(self):
        self.cpus += 1

    def aloca_disco(self, numeroDiscos: int) -> bool:
        if self.discos - numeroDiscos >= 0:
            self.discos -= numeroDiscos
            return True
        return False

    def _libera_disco(self, numeroDiscos: int):
        self.discos += numeroDiscos

    # não botei o tipo do processo aqui pq ele tá reclamando de dep cíclica
    def adiciona_processo_execucao(self, processo) -> bool:
        if len(self.executando) >= self.max_cpus:
            return False

        self.executando.append(processo)
        return True
