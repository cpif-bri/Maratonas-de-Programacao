palavra = input()
palavra = palavra.upper()

s = [0] * 26

impar = 0
palindromo = 1

for letra in palavra:
    s[ord(letra) - 65] += 1

for i in range(26):
    impar += s[i] % 2
    if impar > (len(palavra) % 2):
        palindromo = 0
        break

print(palindromo)