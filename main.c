#include <stdio.h>
#include <stdlib.h>

#include "escalonador.h"

int main (void) {
    TProcesso teste = {
        .numero_processo = 1,
        .tempo_de_chegada = 1,
        .prioridade = 1,
        .tempo_de_processador = 1,
        .memoria = 1,
        .unidade_disco = 1,
        .prox = NULL
    };

    TFila *fila = cria_fila(2);

    fila = adiciona_processo(fila, teste);
    fila = adiciona_processo(fila, teste);

    printf("tamanho: %i\n", fila->tamanho);

    fila = adiciona_processo(fila, teste);
    fila = adiciona_processo(fila, teste);

    printf("tamanho: %i\n", fila->tamanho);

    for (int i = 0; i <= fila->fim; i++) {
        printf("item %i : %i\n", i, fila->itens[i].memoria);
    }

    for (int i = 0; i < 999; i++) {
        teste.numero_processo = i;
        fila = adiciona_processo(fila, teste);
    }

    printf("tamanho: %i\n", fila->tamanho);

    for (int i = 0; i <= fila->fim; i++) {
        printf("item %i : %i\n", i, fila->itens[i].numero_processo);
    }

    TProcesso out = {};

    if (pop_processo(fila, &out) == 0) {
        printf("%i\n", out.numero_processo);
    }

    printf("tamanho: %i\n", fila->fim);

    teste.numero_processo = 9999;
    fila = adiciona_processo(fila, teste);

    for (int i = 0; i <= fila->fim; i++) {
        printf("item %i : %i\n", i, fila->itens[i].numero_processo);
    }

    destroi_fila(fila);

    return 0;
}
