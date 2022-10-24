x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

encontro = False

if(x1 < x2):
    if(v1 > v2):
        if((x2- x1) % (v1 - v2) == 0):
            encontro = True
elif(x2 < x1):
    if(v2 > v1):
        if((x1 - x2) % (v2 - v1) == 0):
            encontro = True
elif(x1 == x2):
    if(v1 == v2):
        encontro = True

if(encontro == True):
    print("SIM")
else:
    print("NAO")