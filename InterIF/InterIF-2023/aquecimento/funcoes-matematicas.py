# Função de Rafael
def r(x, y):
    return ((3 * x) ** 2) + (y ** 2
)
# Função de Beto
def b(x, y):
    return (2 * (x ** 2) )+ ((5 * y) ** 2)

# Função de Carlos
def c(x, y):
    return (-100 * x) + (y ** 3)

lista = input().split(' ')

x = int(lista[0])
y = int(lista[1])

# Exemplos de chamadas das funções
rafael = r(x, y)
beto = b(x, y)
carlos = c(x, y)

print(rafael)
print(beto)
print(carlos)

if(rafael > beto and rafael > carlos):
    print('Rafael ganhou')
elif(beto > rafael and beto > carlos):
    print('Beto ganhou')
else:
    print('Carlos ganhou')
