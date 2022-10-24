#include<stdio.h>
#include<string.h>

typedef int bool;
#define true 1
#define false 0

typedef struct NO {
    char nome[41];
    struct NO *primFilho;
    struct NO *proxIrmao;
} NO;

typedef NO *PONT;

PONT criarNovoNo(char nome[41])
{
    PONT novo = (PONT)malloc(sizeof(NO));
    novo->primFilho = NULL;
    novo->proxIrmao = NULL;
    strcpy(novo->nome, nome);
    return (novo);
}

PONT inicializa(char *nome) {
    return (criarNovoNo(nome));
}

PONT buscaChave(char *ch, PONT raiz) {
    if(raiz == NULL)
        return NULL;
    if(strcmp(raiz->nome, ch) == 0)
        return raiz;

    PONT p = raiz->primFilho;

    while(p)
    {
        PONT resp = buscaChave(ch, p);
        if(resp)
            return (resp);
        p = p->proxIrmao;
    }

    return (NULL);
}

bool insere(PONT raiz, char *novaChave, char *chavePai){
    PONT pai = buscaChave(chavePai, raiz);
    if(!pai)
        return (false);
    PONT filho = criarNovoNo(novaChave);
    PONT p = pai->primFilho;

    if(!p)
        pai->primFilho = filho;
    else
    {
        if(strcmp(filho->nome, p->nome) < 1)
        {
            filho->proxIrmao = p;
            pai->primFilho = filho;
        } else {
            PONT aux = p;
            while(p->proxIrmao && strcmp(filho->nome, p->nome) > 1)
            aux = aux->proxIrmao;

            filho->proxIrmao = aux->proxIrmao;
            aux->proxIrmao = filho;
        }
    }
    return (true);
}


void exibirArvore(PONT raiz)
{
    if(raiz == NULL)
        return;
    printf("%s\n", raiz->nome);
    PONT p = raiz->primFilho;
    while(p)
    {
        exibirArvore(p);
        p = p->proxIrmao;
    }
    printf("");
}


int main () {
    char nome1[41], nome2[41];

    scanf("%s", &nome1);
    PONT raiz = inicializa(nome1);

    scanf("%s %s", &nome1, &nome2);
    while(strcmp(nome1, "fim") != 0 && strcmp(nome2, "entrada") != 0)
    {
        insere(raiz, nome1, nome2);
        scanf("%s %s", &nome1, &nome2);
    }

    scanf("%s", &nome1);
    PONT no = buscaChave(nome1, raiz);
    exibirArvore(no);

    return 0;
}
