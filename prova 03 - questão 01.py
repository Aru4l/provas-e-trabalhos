# O número 3025 possui a seguinte característica: 25 + 30 = 55. 55^2 = 3025. 
# Faça um programa que pesquise e imprima todos os números de quatro algarismos que apresentam tal característica. 
# Utilize uma função para determinar se um número se comporta como o 3025.

def analise_numero(valor):
    valor_str = str(valor)
    parte1 = int(valor_str[:2])
    parte2 = int(valor_str[2:])
    return (parte1 + parte2) ** 2 == valor

def encontra_numeros():
    for numero in range (1000, 10000):
        if analise_numero(numero):
            print(numero)

encontra_numeros()
