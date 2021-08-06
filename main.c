#include <stdio.h>
#include <stdlib.h>

#include "escalonador.h"

int main (void) {
    // inicializa "computador"
    TRecursos pc = {
        .cpus = 4,
        .mem = 16000,
        .disks = 2,
    };

    // NOTE(Geraldo)
    // To assumindo que o arquivo de entrada tá ordenado pelo
    // primeiro valor (tempo de chegada). Se esse não for o
    // caso vai ser necessário fazer uma função de sort
    // pelo arrival time.
    TFila *arrived = parsear_arquivo_entrada("entrada_teste.txt");

    TProcesso proc = {};

    while (pop_processo(arrived, &proc) == 0) {
        printf("%i\n", proc.tempo_de_chegada);
    }

    destroi_fila(arrived);

    return 0;
}
