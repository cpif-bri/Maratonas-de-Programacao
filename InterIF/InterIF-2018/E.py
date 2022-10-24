from time import time

def isPrime(n, i = 2): 
    # Base cases
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
 
    # Check for next divisor
    return isPrime(n, i + 1)

e = int(input())

st = time()
cont = 0

for i in range(e):
    if(isPrime(i+1) == True):
        cont+=1

print(cont)
et = time()
# get the execution time
elapsed_time = (et - st)
print('Execution time:', elapsed_time, 'seconds')