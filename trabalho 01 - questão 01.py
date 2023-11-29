def inicializar_matriz():
    return [[0] * 10 for _ in range(6)]

def realizar_locacoes(matriz):
    while True:
        tipo_filme = int(input("Informe o tipo do filme (1 - comédia, 2 - drama, 3 - desenho animado, 4 - suspense, 5 - aventura, 6 - musical): "))
        
        if tipo_filme < 0 or tipo_filme > 6:
            break
        
        codigo_dvd = int(input("Informe o código do DVD: "))
        
        matriz[tipo_filme - 1][codigo_dvd - 1] += 1

def imprimir_matriz(matriz):
    for i, tipo_filme in enumerate(["Comédia", "Drama", "Desenho Animado", "Suspense", "Aventura", "Musical"]):
        for j in range(10):
            print(f"{tipo_filme} - DVD {j + 1}: {matriz[i][j]} locações")
    
def mais_locados(matriz):
    max_locacoes = 0
    max_locacoes_info = None
    
    for i in range(6):
        for j in range(10):
            if matriz[i][j] > max_locacoes:
                max_locacoes = matriz[i][j]
                max_locacoes_info = (i + 1, j + 1)
    
    tipo_filme, codigo_dvd = max_locacoes_info
    print(f"Os DVDs mais locados são do tipo {tipo_filme} - DVD {codigo_dvd} com {max_locacoes} locações.")

def tipo_mais_procurado(matriz):
    total_por_tipo = [sum(matriz[i]) for i in range(6)]
    tipo_mais_procurado = total_por_tipo.index(max(total_por_tipo)) + 1
    print(f"O tipo de filme mais procurado é o tipo {tipo_mais_procurado}.")

def total_locacoes(matriz):
    total = sum(sum(matriz[i]) for i in range(6))
    print(f"O número total de locações de DVDs é {total}.")


matriz_locacoes = inicializar_matriz()
realizar_locacoes(matriz_locacoes)

print("=-" * 30)
print("\nMatriz de Locações:")
imprimir_matriz(matriz_locacoes)

print("=-" * 30)
mais_locados(matriz_locacoes)
tipo_mais_procurado(matriz_locacoes)
total_locacoes(matriz_locacoes)
