#ifndef ESCALONADOR_H_
#define ESCALONADOR_H_

#include <stdint.h>

// NOTE(Geraldo)
// Static pode ter 3 interpretações diferentes.
// Eu considero essas 3 as que fazem mais sentido.
// Provavelmente vamos usar só o internal, mas
// deixei o resto definido caso for preciso.
// local_persist: mantém o valor da variável
//                depois de sair de um escopo.
// global_variable: é melhor definir varáveis globais
//                  como static, pra ela não poder ser
//                  acessada fora da .c que foi definida.
// internal: mesma coisa pra variável, só que usado em
//           funções. definindo uma função como static
//           ela não pode ser acessada fora do .c
//           em que ela foi definida. (o mais útil)
#define local_persist static
#define global_variable static
#define internal static

// NOTE(Geraldo)
// Boa prática fazer typedefs pros primitivos
// ainda mais quando se trata de int. A lib
// stdint é útil pra usar inteiros de tamanho
// fixo, isso evita possíveis problemas entre
// arquiteturas de processadores (o int padrão
// tem tamanho variado dependendo da cpu).
typedef int32_t i32;
typedef int8_t i8;

typedef uint32_t u32;
typedef uint8_t u8;

typedef struct Processo {
    i32 numero_processo;
    i32 tempo_de_chegada;
    i32 prioridade;
    i32 tempo_de_processador;
    i32 memoria;
    i32 unidade_disco;
    struct Processo *prox;
} TProcesso;

typedef struct Recursos {
    i32 cpu1;
    i32 cpu2;
    i32 cpu3;
    i32 cpu4;
    i32 memoria;
    i32 unidade_disco;
} TRecursos;

typedef struct Fila {
    TProcesso *itens;
    i32 fim;
    i32 inicio;
    i32 tamanho;
} TFila;

TFila* cria_fila(i32 tamanho_inicial);

void adiciona_processo(TFila *fila, TProcesso *processo);
TProcesso* pop_processo(TFila *fila);
TFila* cresce_fila(TFila *fila, i32 quantidade);

void destroi_fila(TFila *fila);

#endif // ESCALONADOR_H_
