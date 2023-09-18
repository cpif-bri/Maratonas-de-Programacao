from operator import itemgetter

# Lê os valores iniciais
nCompetidores, voltas, inv = map(int, input().split())

# Inicializa a lista de competidores
competidores = []

# Lê os nomes dos competidores
for i in range(nCompetidores):
    nome = input().strip()
    sigla = nome[:3].upper()
    competidores.append([nome, sigla, []])

# Lê os tempos das voltas
for i in range(voltas):
    s = input().split()
    sigla = s[0]
    tempo = s[1]
    for i, competidor in enumerate(competidores):
        if sigla == competidor[1]:
            competidor[2].append((tempo, i))

for i in range(inv):
    s = input().split()
    sigla = s[0]
    tempo = s[1]
    removeu = False
    for competidor in competidores:
        if sigla == competidor[1]:
            for t in range(len(competidor[2])):
                if competidor[2][t][0] == tempo:
                    competidor[2].pop(t)
                    break
        if removeu:
            break

# Ordena os competidores com base nos tempos mais cedo, com desempate pelo tempo mais cedo da primeira volta
competidores.sort(key=lambda x: (x[2][0], x[2].index(x[2][0])))

for i, competidor in enumerate(competidores):
    print(i + 1, competidor[0], competidor[2][0][0])