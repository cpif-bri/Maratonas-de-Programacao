x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

xf1 = x1 + v1
xf2 = x2 + v2

if(xf1 > xf2):
    dif = xf1 - xf2
    if(dif > v2):
        print("NAO")
    else:
        print("SIM")
elif(xf1 < xf2):
    dif = xf2 - xf1
    if(dif > v1):
        print("NAO")
    else:
        print("SIM")
else:
    print("SIM")