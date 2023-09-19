n = int(input())

vals = []

for i in range(n):
    f = int(input())
    vals.append(f)

v = int(input())

vals.sort(reverse=True)

cont = 0
i = 0

for i in range(len(vals)):
    cont += v // vals[i]
    v -= (v // vals[i]) * vals[i]

print(cont)