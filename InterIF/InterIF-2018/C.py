n = int(input())
angulos = [int(x) for x in input().split(" ")]

i = n % 359
if(i not in angulos):
    print(i)
else: 
    while(i < 360):
        if(i not in angulos):
            print(i)
            break
        elif(i + 5 > 359):
            i = 1
        else:
            i+=5