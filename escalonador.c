#include <stdlib.h>
#include <string.h>

#include "escalonador.h"

TFila* cria_fila(int tamanho_inicial) {
    TFila *new = (TFila*) malloc(sizeof(TFila));
    TProcesso *array_procs = (TProcesso*) malloc(sizeof(TProcesso) * tamanho_inicial);

    new->inicio = 0;
    new->fim = -1;
    new->tamanho = tamanho_inicial;
    new->itens = array_procs;

    return new;
}

TFila* adiciona_processo(TFila *fila, TProcesso processo) {
    if (fila->fim == (fila->tamanho) - 1) {
        TFila *nova = cresce_fila(fila, 10);

        nova->fim += 1;
        nova->itens[nova->fim] = processo;

        return nova;
    } else {
        fila->fim += 1;
        fila->itens[fila->fim] = processo;

        return fila;
    }
}

// NOTE(Geraldo)
// Retorna 0 no sucesso e > 0 caso falhe.
// To usando o padrão do linux nesse caso.
u8 pop_processo(TFila *fila, TProcesso *out) {
    if (fila->fim == -1) {
        return 1;
    }

    TProcesso atual = fila->itens[fila->fim];

    fila->fim -= 1;

    *out = atual;

    return 0;
}

TFila* cresce_fila(TFila *fila, i32 quantidade) {
    i32 tamanho_novo = fila->tamanho + quantidade;
    TProcesso *new_procs = (TProcesso*) malloc(sizeof(TProcesso) * tamanho_novo);

    // copia o conteúdo antigo dos itens para a nova array maior
    memcpy(new_procs, fila->itens, sizeof(TProcesso) * fila->tamanho);

    free(fila->itens);
    fila->itens = new_procs;
    fila->tamanho = tamanho_novo;

    return fila;
}

void destroi_fila(TFila *fila) {
    free(fila->itens);
    free(fila);
    return;
}

