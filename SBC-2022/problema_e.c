
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int n;
    int flechas = 0;
    scanf("%d", &n);

    int *h;
    h = (long int*)malloc(1000001*sizeof(long int));
    int i = 0;
    int balao;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &balao);
        if(h[balao + 1] == 0){
            flechas+=1;
        }
        else {
            h[balao+1] -= 1;
        }
        h[balao] += 1;
    }

    printf("%d\n", flechas);

    return 0;
}
