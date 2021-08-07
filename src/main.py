from classes.Processo import Processo
from classes.Recursos import Recursos
from utils.parser import parseTxt


def main():
    processos = parseTxt("~/../entrada_teste.txt")
    for processo in processos:
        print(processo)


if __name__ == "__main__":
    main()
