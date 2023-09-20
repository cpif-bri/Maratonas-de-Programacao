import math

N = int(input())

cedulas =[]

while N > 0:
    if(N == 0):
        break
    N = N - 1
    cedulas.append(int(input()))

cedulas.sort()

val = int(input())

qtd = 0

while(val > 0):
    cur = cedulas.pop()
    res = math.floor(val / cur)
    val -= res * cur
    qtd += res

print(qtd)