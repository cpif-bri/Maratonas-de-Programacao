dados = input();
numerosComoString = dados.split(" ")
numeros = [float(numero) for numero in numerosComoString]
x, y = numeros
r = pow((3*x),2) + pow(y,2);
b = 2*pow(x,2) + pow((5*y),2);
c = -100 * x + pow(y,3);
if b > r and b > c:
    print("Beto ganhou");
elif r > b and r > c:
    print("Rafael ganhou");
else:
    print("Carlos ganhou");