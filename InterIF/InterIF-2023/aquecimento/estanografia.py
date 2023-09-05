#Problema A - Esteganografia

texto = input()

maiuscula = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
minuscula = ('abcdefghijklmnopqrstuvwxyz')

mensagem = []
indice = 7
decifra = 0

for letra in texto:
    if letra in maiuscula:
        decifra += 2**indice
        indice -= 1
    elif letra in minuscula:
        indice -= 1

    if indice == -1:
        indice = 7
        mensagem.append(decifra)
        decifra = 0

for letra in mensagem:
    if(letra != 0):
        print(chr(letra), end='')
print('')