import math

def calcular_forcas(tracao, angulo):
    
    # Convertendo o ângulo de graus para radianos
    
    angulo_radianos = math.radians(angulo)

    # Calculando as componentes da força
    
    forca_horizontal = tracao * math.cos(angulo_radianos)
    forca_vertical = tracao * math.sin(angulo_radianos)

    return forca_horizontal, forca_vertical

# Testando a função
tracao = float(input("Digite o valor da tração: ")) # em Newtons
angulo = float(input("Digite o valor do ângulo: "))  # em graus
forca_horizontal, forca_vertical = calcular_forcas(tracao, angulo)

#imprimindo os  valores
print(f"Força Horizontal: {forca_horizontal} N")
print(f"Força Vertical: {forca_vertical} N")
