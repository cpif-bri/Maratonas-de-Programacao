
while True:
    try:
        n = int(input())
        passos = 0
        
        while n != 1:
            if n%2 == 0:
                n = n/2
            else:
                n = n*3 + 1
            passos += 1
            
        print(passos)
    except EOFError:
        break