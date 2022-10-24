alfabeto = [0]*26

palavra = input().lower()

for letra in palavra:
    alfabeto[ord(letra) - 97] += 1

tolera = 0
if len(palavra)%2 == 1:
    tolera = 1

impar = 0
for letra in alfabeto:
    if letra%2 == 1:
        impar += 1

if impar > tolera:
    print('0')
else:
    print('1')

