from dataclasses import dataclass


@dataclass(init=True)
class Recursos:
    cpus: int = 4
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
