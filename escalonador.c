#include <stdio.h>
#include <stdlib.h>

#include "escalonador.h"

typedef struct Processo {
    int numero_processo;
    int tempo_de_chegada;
    int prioridade;
    int tempo_de_processador;
    int memoria;
    int unidade_disco;
    struct Processo *prox;
} TProcesso;

typedef struct Recursos {
    int cpu1;
    int cpu2;
    int cpu3;
    int cpu4;
    int memoria;
    int unidade_disco;
} TRecursos;

typedef struct fila {
    TProcesso *inicio;
    TProcesso *fim;
} TFila;
