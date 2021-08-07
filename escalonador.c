#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "escalonador.h"

TFila* cria_fila(i32 tamanho_inicial) {
    TFila *new = (TFila*) malloc(sizeof(TFila));
    TProcesso *array_procs = (TProcesso*) malloc(sizeof(TProcesso) * tamanho_inicial);

    new->inicio = 0;
    new->fim = -1;
    new->tamanho = tamanho_inicial;
    new->itens = array_procs;

    return new;
}

void adiciona_processo(TFila *fila, TProcesso processo) {
    if (fila->fim == (fila->tamanho - 1)) {
        cresce_fila(fila, 10);
        fila->fim += 1;
        fila->itens[fila->fim] = processo;
    } else {
        fila->fim += 1;
        fila->itens[fila->fim] = processo;
    }
}

// NOTE(Geraldo)
// Retorna 0 no sucesso e >0 caso falhe.
// To usando o padrão do linux nesse caso.
u8 pop_processo(TFila *fila, TProcesso *out) {
    // Caso estiver vazia
    if (fila->fim == -1) {
        return 1;
    }

    // Caso for o último item da fila
    if (fila->inicio == fila->fim) {
        TProcesso atual = fila->itens[fila->inicio];

        fila->inicio = 0;
        fila->fim = -1;
        *out = atual;

        return 0;
    }

    TProcesso atual = fila->itens[fila->inicio];

    fila->inicio += 1;

    *out = atual;

    return 0;
}

TProcesso peek_processo(TFila *fila) {
    return fila->itens[fila->inicio];
}

void cresce_fila(TFila *fila, i32 quantidade) {
    i32 tamanho_novo = fila->tamanho + quantidade;
    TProcesso *new_procs = (TProcesso*) malloc(sizeof(TProcesso) * tamanho_novo);

    // copia o conteúdo antigo dos itens para a nova array maior
    memcpy(new_procs, fila->itens, sizeof(TProcesso) * fila->tamanho);

    free(fila->itens);
    fila->itens = new_procs;
    fila->tamanho = tamanho_novo;
}

void destroi_fila(TFila *fila) {
    free(fila->itens);
    free(fila);
    return;
}

TFila* parsear_arquivo_entrada(char *nome) {
    FILE *arquivo = fopen(nome, "r");
    if (arquivo == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    TFila *fila = cria_fila(50);

    u32 arrival, priority, cpu_time, mem, disk;
    i32 pid = 1;
    while (
        fscanf(
            arquivo,
            "%i, %i, %i, %i, %i",
            &arrival, &priority, &cpu_time, &mem, &disk
        ) != EOF
    ) {
        TProcesso novo_processo = {
            .numero_processo = pid,
            .tempo_de_chegada = arrival,
            .prioridade = priority,
            .tempo_de_processador = cpu_time,
            .memoria = mem,
            .unidade_disco = disk,
        };
        adiciona_processo(fila, novo_processo);
        pid++;
    }

    fclose(arquivo);
    return fila;
}

TFilasDePrioridade gerar_filas_prioridades(TFila *fila) {
    TFila *p0 = cria_fila(fila->tamanho);
    TFila *p1 = cria_fila(fila->tamanho);
    TProcesso proc = {};

    while (pop_processo(fila, &proc) == 0) {
        if (proc.prioridade == 0) adiciona_processo(p0, proc);
        else if (proc.prioridade == 1) adiciona_processo(p1, proc);
    }

    TFilasDePrioridade resp = {
        .p0 = p0,
        .p1 = p1,
    };

    return resp;
}
