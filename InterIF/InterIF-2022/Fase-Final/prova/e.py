def primo(n, num = 2):
    if(n <= 2):
        if(n == 1 or n == 0):
            return False 
        else: 
            return True
    else:
        if(num == n):
            return True
        if(n % num == 0):
            return False
        else:
            return primo(n, num+1)

n = int(input())
album = [0] * int(n+1)
erro = False
figs = [int(x) for x in input().split(" ")]

for fig in figs:
    if(fig > n):
        erro = True
    else:
        album[fig] += 1

if(erro == False):
    coladas = []
    especiais = []

    for i in range(len(album)):
        if(album[i] > 0):
            coladas.append(i)
            if(primo(i) == True):
                especiais.append(i)
        
    coladas.sort()
    especiais.sort()

    for i in range(len(coladas)):
        if(i < len(coladas)-1):
            print(coladas[i], end=' ')
        else:
            print(coladas[i], end='\n')

    for i in range(len(especiais)):
        if(i < len(especiais)-1):
            print(especiais[i], end=' ')
        else:
            print(especiais[i], end='\n')
else:
    print("ERRO")