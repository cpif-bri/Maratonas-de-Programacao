# import time
n, nl = input().split()
#Conta o tempo de execução
# timeEx = time.time()
n = int(n)
nl = int(nl)
l = []
alfa = "abcdefghijklmnopqrstuvwxyz"
for x in range(n):
    l.append(input())
posib = []
for p in l:
    for x in alfa:
        palavra = p
        posib.append(palavra.replace('*',x))
maior = 0
palavra = ''
for p in posib:
    if posib.count(p) > maior:
        maior = posib.count(p)
        palavra = p
print(palavra, maior)
# print("--- %s seconds ---" % (time.time() - timeEx))






