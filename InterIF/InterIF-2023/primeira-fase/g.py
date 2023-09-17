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
    for competidor in competidores:
        if sigla == competidor[1]:
            competidor[2].append(tempo)

# Remove as voltas inválidas
for i in range(inv):
    s = input().split()
    sigla = s[0]
    tempo = s[1]
    for competidor in competidores:
        if sigla == competidor[1] and tempo in competidor[2]:
            competidor[2].remove(tempo)

# Ordena os competidores com base nos tempos
competidores.sort(key=lambda x: (x[2], x[0]))

# Imprime a classificação
for i, competidor in enumerate(competidores):
    print(i + 1, competidor[0], competidor[2][0])
