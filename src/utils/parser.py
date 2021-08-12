from classes.Processo import Processo


def txtParaListaDeProcessos(caminho: str) -> list[Processo]:
    arquivo = open(caminho, "r")
    linhas = arquivo.readlines()
    lista_processos: list[Processo] = []
    pid = 0
    for linha in linhas:
        args = list(map(int, linha.split(", ")))
        processo = Processo(pid, args[0], args[1], args[2], args[3], args[4])
        lista_processos.append(processo)
        pid += 1

    return sorted(lista_processos, key=lambda i: i.tempo_de_chegada)
