# PROBLEMA B - V INTERIF 2022 - TRIATLO

from time import time


def propaga(matriz, n, ponto, passou):
    passou[ponto] = True
    for i in range(n):
        if matriz[ponto][i]:
            if not passou[i]:
                propaga(matriz, n, i, passou)
    return

def triatlo(listaPontos):
    for passou in listaPontos:
        if not passou:
            return True
    return False

n, m = [int(x) for x in input().split(' ')]

passou = [False]*n
matriz = []

for i in range(n): matriz.append(passou[:])

for i in range(m):
    ponto1, ponto2 = [int(x) for x in input().split(' ')]
    matriz[ponto1-1][ponto2-1] = True
    matriz[ponto2-1][ponto1-1] = True

ini = time()

if n > 2:
    propaga(matriz, n, 0, passou)
    if(triatlo(passou)):
        print('triatlo')
    else:
        print('ciclismo')
else:
    print('corrida')

end = time()

print(f'Tempo passado {end-ini} seconds')
