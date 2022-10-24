def fatorial(n):
    if(n == 1):
        return 1
    else:
        return n * fatorial(n-1)

n = int(input())
x = int(input())

fat = []

for i in range(x):
    temp = int(input())
    fat.append(int(str(fatorial(temp))[:n]))

fat.sort()
print("INICIO")
for num in fat:
    print(num)
print("FIM")
    
