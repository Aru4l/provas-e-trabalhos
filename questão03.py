def le_matriz():
    matriz = []
    for c in range(6):
        linha = [float(input(f"Insira valor para a posição ({c+1}, {i+1}): ")) for i in range(6)]
        matriz.append(linha)
    return matriz

def media_area_cinza(matriz):
    soma = 0
    contador = 0
    for i in range(1, 5):
        for j in range(1, 5):
            soma += matriz[i][j]
            contador += 1
    return soma / contador

def maior_elemento(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior

def valor_contido(matriz, valor):
    for linha in matriz:
        if valor in linha:
            return True
    return False

def diagonal_principal(matriz):
    diagonal = [matriz[i][i] for i in range(6)]
    return diagonal

def menu():
    matriz = le_matriz()

    while True:
        print("=-" * 20)
        print("\n::. Menu .::")
        print("1. Calcular média da área cinza")
        print("2. Encontrar maior elemento na matriz")
        print("3. Verificar se um valor está contido na matriz")
        print("4. Mostrar elementos da diagonal principal")
        print("5. Sair")

        opcao = input("Opções (1-5): ")
        print("=-" * 20)
        if opcao == '1':
            media = media_area_cinza(matriz)
            print(f"A média da área cinza é {media}")

        elif opcao == '2':
            maior = maior_elemento(matriz)
            print(f"O maior elemento na matriz é {maior}")

        elif opcao == '3':
            valor = float(input("Insira o valor a ser verificado na matriz: "))
            if valor_contido(matriz, valor):
                print(f"O valor {valor} existe na matriz.")
            else:
                print(f"O valor {valor} não existe na matriz.")

        elif opcao == '4':
            diagonal = diagonal_principal(matriz)
            print("Elementos da diagonal principal:", diagonal)

        elif opcao == '5':
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
