N = int(input())
X = int(input())

pessoas = [i for i in range(1,N+1)]
mortes = 0
i = 1
while(len(pessoas) > 1):
    mortes+=1
    if(mortes == X):
        print(f'Morte {mortes}: {pessoas[i]}')
    del pessoas[i]
    if(i > len(pessoas) - 1):
        i = 1
    elif(i + 1 > len(pessoas) -1 ):
        i = 0
    else:
        i+=1

print(f'Sobrevivente: {pessoas[0]}')