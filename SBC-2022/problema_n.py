from operator import itemgetter


def retiraPontas(frente, costas):
    if((frente[0] + costas[0]) >= (frente[len(frente)-1]+costas[len(costas)-1])):
        ponta = [frente[0], costas[0]]
        del frente[0]
        del costas[0]
    else: 
        ponta = [frente[len(frente)-1],costas[len(costas)-1]]
        del frente[len(frente)-1]
        del costas[len(costas)-1]
    return ponta, frente, costas

n = int(input())

frente = [int(x) for x in input().split(" ")]
costas = [int (x) for x in input().split(" ")]
pontas = []

k, l = (int(x) for x in input().split(" "))
soma = 0

for i in range(k):
    pontasT, frente, costas = retiraPontas(frente, costas)
    soma+=pontasT[0]
    pontas.append(pontasT)

pontaSorted = sorted(pontas, key=itemgetter(1) , reverse=True)

for i in range(l):
    soma += pontaSorted[i][1]

print(soma)