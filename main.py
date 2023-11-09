def tresmaiores(A, B, C, D):
    elementos = [A, B, C, D]
    elementos.sort(reverse=True)
    soma = elementos[0] + elementos[1] + elementos[2]
    return soma, elementos

while True: 
    try: 
        A = int(input("Digite o 1° número: "))
        B = int(input("Digite o 2° número: "))
        C = int(input("Digite o 3° número: "))
        D = int(input("Digite o 4° número: "))

        soma, elementos = tresmaiores(A, B, C, D)
        print(f"A soma dos valores é {soma}")
        print(f"A lista de elementos em ordem descrente é {elementos}")

        pergunta = (input("Deseja continuar (S/N)?")).upper()
        if pergunta == "N": 
            break
    except ValueError:
        print("Por favor, insira valores válidos!")