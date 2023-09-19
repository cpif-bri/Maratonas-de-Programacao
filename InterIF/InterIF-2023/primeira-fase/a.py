s = input()

cont = 0

vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

for c in s:
    if c in vogais:
        cont += 1

print('frasco', cont % 3)