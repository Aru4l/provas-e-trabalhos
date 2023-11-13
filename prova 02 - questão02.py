def ler_matriz():
    matriz = []
    for c in range(5):
        linha = []
        for i in range(5):
            elementos = int(input(f"Digite um valor para a posição ({c+1}, {i+1}): "))
            linha.append(elementos)
        matriz.append(linha)
    return matriz

def soma_matriz(matriz1, matriz2):
    resultado = []
    for c in range(5):
        linha = []
        for i in range(5):
            soma = matriz1[c][i] + matriz2[c][i]
            linha.append(soma)
        resultado.append(linha)
    return resultado


print(" > Matriz A < ")
A = ler_matriz()

print(" > Matriz B < ")
B = ler_matriz()

print(" > Matriz C < ")
C = ler_matriz()

print(" > Matriz D < ")
D = ler_matriz()

soma_AB = soma_matriz(A, B)
soma_CD = soma_matriz(C, D)
soma_AC = soma_matriz(A, C)

print("=-" * 20)
print("\nSoma A + B: ")
for linha in soma_AB:
    print(linha)

print("\nSoma C + D: ")
for linha in soma_CD:
    print(linha)

print("\nSoma A + C: ")
for linha in soma_AC:
    print(linha)
