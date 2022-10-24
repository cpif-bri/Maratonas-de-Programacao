matriz = [[],[],[]]

for i in range(3):
    matriz[i] = input()

if (matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X'):
    print("X venceu!")

elif (matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X'):
    print("X venceu!")

elif (matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X'):
    print("X venceu!")

elif (matriz[1][0] == 'X' and matriz[1][1] == 'O' and matriz[1][2] == 'X'):
    print("X venceu!")

elif (matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X'):
    print("X venceu!")

elif (matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X'):
    print("X venceu!")

elif (matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X'):
    print("X venceu!")

elif (matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X'):
    print("X venceu!")

elif (matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X'):
    print("X venceu!")

elif (matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O'):
    print("O venceu!")

elif (matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O'):
    print("O venceu!")

elif (matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O'):
    print("O venceu!")

elif (matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O'):
    print("O venceu!")

elif (matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O'):
    print("O venceu!")

elif (matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O'):
    print("O venceu!")

elif (matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O'):
    print("O venceu!")
else:
    for i in range(3):
        if('#' in matriz[i]):
            print("Jogo em andamento")
        exit(0)
    print("Velha")
