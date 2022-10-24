resultado = (10000001, 10000002, 10000003, 9999997, 9999998, 9999999, 10000000)

def f(x):
    if x >= 10000000:
        return x-3
    else:
        return resultado[x%7]

x = int(input())
print(f(x))