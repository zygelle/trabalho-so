from classes.Processo import Processo
from classes.Recursos import Recursos
from utils.parser import txtParaListaDeProcessos
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(ROOT_DIR, "entrada_teste.txt")


def main():
    processos = txtParaListaDeProcessos(ENTRY_FILE)
    for processo in processos:
        print(processo)


if __name__ == "__main__":
    main()
