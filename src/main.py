from classes.Processo import Processo
from classes.Recursos import Recursos
from utils.parser import txtParaListaDeProcessos
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(ROOT_DIR, "entrada_teste.txt")


class UserOptions:
    comando_atual: list[str] = []
    executando: bool = True
    momento_atual: int = 0
    comandos_validos: tuple = (
        "p",
        "prox",
        "q",
        "quit",
        "h",
        "help",
    )


def mostraInterfacePrincipal(recursos: Recursos, opts: UserOptions) -> None:
    print(
        "Recursos atuais: cpu {}, mem {}, discos {}".format(
            recursos.cpus, recursos.memoria, recursos.discos
        )
    )
    print("Momento atual: {}".format(opts.momento_atual))
    print("Filas:")
    print()


def pegaInputUsuario(opts: UserOptions) -> None:
    user_in = input("> ").split(" ")
    while not user_in[0] in opts.comandos_validos:
        print("Por favor escolha um comando válido. Use help (h).")
        print()
        user_in = input("> ").split(" ")
    
    opts.comando_atual = user_in


def mostraAjuda() -> None:
    print("prox <quantidade> (p): avança a quantidade de tempo especificada")
    print("quit (q): fecha o programa")
    print("help (h): mostra esse menu")
    print()


def processaInputUsuario(opts: UserOptions) -> None:
    if opts.comando_atual[0] == "p" or opts.comando_atual[0] == "prox":
        pass
    elif opts.comando_atual[0] == "q" or opts.comando_atual[0] == "quit":
        opts.executando = False
    elif opts.comando_atual[0] == "h" or opts.comando_atual[0] == "help":
        mostraAjuda()


def main():
    opts = UserOptions()
    recursos = Recursos()
    processos = txtParaListaDeProcessos(ENTRY_FILE)

    mostraInterfacePrincipal(recursos, opts)
    while opts.executando:
        pegaInputUsuario(opts)
        processaInputUsuario(opts)


if __name__ == "__main__":
    main()
