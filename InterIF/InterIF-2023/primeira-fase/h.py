
n = []

for i in range(0,4):
    n.append(int(input()))

liberacao = True

for i in range(1,4):
    if n[i] < n[i-1]:
        liberacao = False

if n[3] != n[0] + n[1] + n[2]:
    liberacao = False

if liberacao:
    print('LIBERADO')
else:
    print('NEGADO')