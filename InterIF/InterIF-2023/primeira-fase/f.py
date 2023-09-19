from operator import itemgetter, attrgetter

e = int(input())
j = int(input())

# (NOME, P, N, S)
tab = []
placar = []
times = []

for i in range(j):
    inf = input().split(' ')
    time1 = inf[0]
    time2 = inf[4]
    pont1 = int(inf[1])
    pont2 = int(inf[3])

    if time1 not in times:
        times.append(time1)
        placar.append([time1, 0, 0, 0])
    if time2 not in times:
        times.append(time2)
        placar.append([time2, 0, 0, 0])
    
    if pont1 > pont2:
        tab.append([time1, 3, 1, pont1 - pont2])
        tab.append([time2, 0, 0, pont2 - pont1])
    elif pont2 > pont1:
        tab.append([time2, 3, 1, pont2 - pont1])
        tab.append([time1, 0, 0, pont1 - pont2])
    else:
        tab.append([time2, 1, 0, 0])
        tab.append([time1, 1, 0, 0])


for i in range(len(placar)):
    for j in range(len(tab)):
        if placar[i][0] == tab[j][0]:
            placar[i][1] += tab[j][1]
            placar[i][2] += tab[j][2]
            placar[i][3] += tab[j][3]

dataSort = sorted(placar, key=itemgetter(1,2,3), reverse=True)

for tim in dataSort:
    print(tim[0], tim[1], tim[2], tim[3])