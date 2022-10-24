n = int(input())
seq = input()
a = 0
cons = 0

# percorre a string por cada letra
for letra in seq:
    # se encontrar um 'a' adiciona na variavel de controle + 1
    if(letra == 'a'):
        cons += 1
    # se passar por uma letra que não é 'a'
    else:
        # se ao encontrar outra letra alem do 'a' e já houver encontrado mais do que 1 'a'
        if(cons > 1):
            # atribui a variavel de controle somada a variavel de controle total a ela mesma
            a+=cons
        # zera a variavel de controle
        cons = 0

# para verificação dos 'a's que terminam a string
if(cons > 1):
    a+=cons
    
print(a)