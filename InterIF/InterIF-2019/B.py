# -1 lado oeste, -2 lado sul, -3 o lado norte e -4 representa o lado leste, 

aeronaves = [[], [], [], []]
qtdAeronaves = 0
ordem = []
coord = 0

temp = input()
while(temp != '0'):
    if(temp[0] == 'A'):
        if(coord == '-1'):
            aeronaves[0].append(temp)
        if(coord == '-2'):
            aeronaves[1].append(temp)
        if(coord == '-3'):
            aeronaves[2].append(temp)
        if(coord == '-4'):
            aeronaves[3].append(temp)
        qtdAeronaves += 1
    else:
        coord = temp
    temp = input()

for i in range(qtdAeronaves):
    if((i + 1) % 4 == 1):
        if(len(aeronaves[0]) > 0):
            ordem.append(aeronaves[0][0])
            del aeronaves[0][0]
    if((i + 1) % 4 == 2):
        if(len(aeronaves[2]) > 0):
            ordem.append(aeronaves[1][0])
            del aeronaves[1][0]
    if((i + 1) % 4 == 3):
        if(len(aeronaves[1]) > 0):
            ordem.append(aeronaves[2][0])
            del aeronaves[2][0]
    if((i + 1) % 4 == 0):
        if(len(aeronaves[3]) > 0):
            ordem.append(aeronaves[3][0])
            del aeronaves[3][0]

print(ordem)