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
    TProcesso *inicio;
    TProcesso *fim;
} TFila;


#endif // ESCALONADOR_H_
