def procuraHorizontal(matriz, palavra, l, c):
    ocorrencia = 0
    for i in range(l):
        for j in range(c):
            if(matriz[i][j] == palavra[0]):
                igual = True
                x = 1
                while(x < len(palavra)):
                    if(len(palavra)-1+j) > c or (matriz[i][j+x] != palavra[x]):
                        igual = False
                        break
                    x += 1
                if(igual):
                    ocorrencia += 1
    return ocorrencia

def procuraVertical(matriz, palavra, l, c):
    ocorrencia = 0
    for j in range(c):
        for i in range(l):
            if(matriz[i][j] == palavra[0]):
                igual = True
                x = 1
                while(x < len(palavra)):
                    if((len(palavra)-1+i) > l or matriz[i+x][j] != palavra[x] ):
                        igual = False
                        break
                    x += 1
                if(igual):
                    ocorrencia += 1
    return ocorrencia

l, c = (int(x) for x in input().split(" "))
matriz = []
linha = []
for i in range(l):
    linha = input().split(" ")
    matriz.append(linha.copy())
    linha.clear()

palavras = []

palavras = input().split(" ")

ocorrencias = []

for palavra in palavras:
    ocorrencias.append(procuraHorizontal(matriz, palavra, l, c) + procuraVertical(matriz, palavra, l, c))

for palavra, ocorrencia in zip(palavras, ocorrencias):
    print(f'{palavra}: {ocorrencia}')