def ciclo(n, matriz, p, x):
    for i in range(n):
        if(matriz[x][i] == 1):
            if(ciclo(n, matriz, p, i)):
                return True
    return False

n,m = (int(x) for x in input().split(" "))

matriz = []
aux = [0] * n

for i in range(n):
    matriz.append(aux.copy())

for i in range(m):
    p1, p2 = (int(x) for x in input().split(" "))
    matriz[p1-1][p2-1] = 1
    matriz[p2-1][p1-1] = 1

achou = False #false é ciclismo

if(n > 2):
    for i in range(n):
        achou = True
        for j in range(n):
            if(matriz[i][j] == 1):
                achou = False    
        if(achou):
            break
    if(achou):
        print("triatlo")
    else:
        print("ciclismo")
else:
    print("corrida")


