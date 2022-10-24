N, x, y = (int(x) for x in input().split(" "))

quad = pow(2,N)
ini = quad // 2

tams = [(0,0),(0,quad),(quad,quad),(quad,0)]

mov = 0

while(x != ini and y != ini):
    # PRIMEIRO QUADRANTE
    if(x <= ini and y >= ini):
        x = int(abs(( x - tams[1][0] )) * 2)
        y = int(abs(( y - tams[1][1] )) * 2)
        mov += 1
    # SEGUNDO QUADRANTE
    elif(x > ini and y > ini):
        x = int(abs(( x - tams[3][0] )) * 2)
        y = int(abs(( y - tams[3][1] )) * 2)
        mov += 1
    # TERCEIRO QUADRANTE
    elif(x < ini and y < ini):
        x = int(abs(( x - tams[0][0] )) * 2)
        y = int(abs(( y - tams[0][1] )) * 2)
        mov += 1
    # QUARTO QUADRANTE
    elif(x >= ini and y <= ini):
        x = int(abs(( x - tams[2][0] )) * 2)
        y = int(abs(( y - tams[2][1] )) * 2)
        mov += 1

print(mov)