#ifndef ESCALONADOR_H_
#define ESCALONADOR_H_

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

typedef struct Fila {
    TProcesso info[50];
    int fim;
    int inicio;
} TFila;

void adiciona_processo(TFila *fila, TProcesso *processo);
TProcesso* pop_processo(TFila *fila);

TFila* cria_fila();
TFila* destroi_fila(TFila *fila);
TFila* cresce_fila(TFila *velha);

#endif // ESCALONADOR_H_
