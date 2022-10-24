n = input()

par = 0
impar = 0

for i in n:
    num = int(i)
    if num%2 == 0:
        par += num
    else:
        impar += num

if par%3 == 0:
    print('S')
else:
    print('N')

if impar%3 == 0:
    print('S')
else:
    print('N')