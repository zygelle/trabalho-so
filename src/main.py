from classes.Processo import Processo
from classes.Recursos import Recursos
from enum import Enum
from utils.parser import txtParaListaDeProcessos
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(ROOT_DIR, "entrada_teste.txt")


class Comando(Enum):
    PROX = 1
    HELP = 98
    QUIT = 99


class UserOptions:
    comando_atual: tuple[Comando, list]
    executando: bool = True
    momento_atual: int = 0
    comandos_validos: tuple[str] = (
        "p",
        "prox",
        "q",
        "quit",
        "h",
        "help",
    )


def mostraInterfacePrincipal(
    processos: Processo, recursos: Recursos, opts: UserOptions
) -> None:
    print(
        "Recursos atuais: cpu {}, mem {}, discos {}".format(
            recursos.cpus, recursos.memoria, recursos.discos
        )
    )
    print("Momento atual: {}".format(opts.momento_atual))
    print("Processos entrando:")
    for p in processos:
        print(
            "pid {}, memoria {}, disco {}".format(
                p.numero_processo, p.memoria, p.unidade_disco
            )
        )

    print("Filas:")

    print()


def processaInputUsuario(opts: UserOptions) -> None:
    user_in = input("> ").split(" ")
    while not user_in[0] in opts.comandos_validos:
        print("Por favor escolha um comando válido. Use help (h).")
        print()
        user_in = input("> ").split(" ")

    if user_in[0] == "p" or user_in[0] == "prox":
        try:
            qtd_tempo = int(user_in[1])
            opts.comando_atual = (Comando.PROX, [qtd_tempo])
        except:
            opts.comando_atual = (Comando.PROX, [1])
    elif user_in[0] == "q" or user_in[0] == "quit":
        opts.comando_atual = (Comando.QUIT, [])
    elif user_in[0] == "h" or user_in[0] == "help":
        opts.comando_atual = (Comando.HELP, [])


def mostraAjuda() -> None:
    print("prox (p) <quantidade>: avança a quantidade de tempo especificada")
    print("quit (q): fecha o programa")
    print("help (h): mostra esse menu")
    print()


def popProcessosNoMomento(
    processos: list[Processo], momento: int
) -> tuple[list[Processo], list[Processo]]:
    p0 = []
    p1 = []

    if not processos:
        return (p0, p1)

    while processos[0].tempo_de_chegada == momento:
        if processos[0].prioridade == 0:
            p0.append(processos.pop(0))
        elif processos[0].prioridade == 1:
            p1.append(processos.pop(0))

        if not processos:
            break

    return (p0, p1)


def main():
    opts = UserOptions()
    recursos = Recursos()
    processos = txtParaListaDeProcessos(ENTRY_FILE)

    mostraInterfacePrincipal([], recursos, opts)
    while opts.executando:
        processaInputUsuario(opts)

        cmd = opts.comando_atual[0]
        if cmd == Comando.PROX:
            for _ in range(opts.comando_atual[1][0]):
                opts.momento_atual += 1

                procs = popProcessosNoMomento(processos, opts.momento_atual)

                mostraInterfacePrincipal(procs[1], recursos, opts)

        elif cmd == Comando.HELP:
            mostraAjuda()
        elif cmd == Comando.QUIT:
            opts.executando = False


if __name__ == "__main__":
    main()
