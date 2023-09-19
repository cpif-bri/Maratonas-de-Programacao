
def primo(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

x = int(input())

primos = []

for n in range(1, x + 1):
    if primo(n):
        primos.append(str(n))

print(' '.join(primos))
