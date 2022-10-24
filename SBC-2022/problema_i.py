string = [int(x) for x in input().split(" ")]
achouLetra = False
for i in range(len(string)):
    if(string[i] == 9):
        achouLetra = True
        break

if(achouLetra == True):
    print("F")
else:
    print("S")