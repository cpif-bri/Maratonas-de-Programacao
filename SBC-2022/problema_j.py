valorCartas = (0,1,2,3,4,5,6,7,8,9,10,10,10,10)
qCartas = [0] * 14

n = int(input())
cJoao = [int(x) for x in input().split(' ')]
cMaria = [int(x) for x in input().split(' ')]

maria = 0
joao = 0

for carta in cMaria:
    qCartas[carta] += 1
    maria += valorCartas[carta]

for carta in cJoao:
    qCartas[carta] += 1
    joao += valorCartas[carta]

comuns = [int(x) for x in input().split()]

for carta in comuns:
    qCartas[carta] +=1
    maria+=valorCartas[carta]
    joao+=valorCartas[carta]

final = -1
for i in range(1,14):
    if(qCartas[i] < 4):
        if(maria+valorCartas[i] == 23):
            final = valorCartas[i]
            break
        elif(maria+valorCartas[i] > 23):
            break
        elif(joao+valorCartas[i]>23):
            final = valorCartas[i]
            break

print(final)
