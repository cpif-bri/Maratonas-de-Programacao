import math

# Função para calcular a área de interseção
def area_intersecao_circulo_triangulo(R):
    # Lados do triângulo semelhante
    lado_1 = 3
    lado_2 = 4
    lado_3 = 5

    # Cálculo da área do setor circular
    area_setor = (1/4) * math.pi * R**2

    # Cálculo da área do triângulo retângulo
    area_triângulo = (1/2) * lado_1 * lado_2

    # Cálculo da área de interseção
    area_intersecao = area_setor - area_triângulo

    return area_intersecao

# Entrada fornecida
R = int(input())

# Exibe o resultado
print(area_intersecao_circulo_triangulo(R))
