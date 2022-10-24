emotes = [':)', '(:', ':O', 'O:', ':D', 'D:', '):', ':(']

texto = input()
cont = 0

for i in range(0, len(texto)- 1):
    if((texto[i] + texto[i+1]) in emotes):
        cont += 1

print(cont)