temp = input()
moedas = []
valorMoedas = [25, 10, 5, 1]
valor = float(temp[2:len(temp)])
valorRestante = valor
sumMoedas = 0.0
i = 0
comprados = 0

for x in input().split(" "):
    moedas.append(int(x))
    sumMoedas += ((moedas[i]*valorMoedas[i]) / 100)
    valorRestante -= ((moedas[i]*valorMoedas[i]) / 100)
    moedas[i] = 0
    if(valorRestante <= 0):
        comprados += 1
        valorRestante = valor - valorRestante
    i += 1


print(comprados)
print(sum(moedas))