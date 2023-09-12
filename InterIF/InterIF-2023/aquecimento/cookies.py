d = int(input())

entrada = input()
saldo = float(entrada.replace("R$", ""))  # Remove o 'R$' do início da entrada
cont = 0

for i in range(d):
    entrada = input()
    valor = float(entrada.replace("R$", ""))
    saldo += valor
    if(saldo != int(saldo)):
        cont+=1

print(cont)