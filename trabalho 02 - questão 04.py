def somatorio_recursivo(vetor, indice):
    if indice == len(vetor) - 1:
        return vetor[indice]
    else:
        return vetor[indice] + somatorio_recursivo(vetor, indice + 1)

vetor = []
for i in range(10):
    elemento = float(input(f"Digite o {i + 1}º elemento do vetor: "))
    vetor.append(elemento)

print("=-" * 30) 
print("Conteúdo do vetor:", vetor)
resultado_somatorio = somatorio_recursivo(vetor, 0)
print("Resultado do somatório: ", resultado_somatorio)