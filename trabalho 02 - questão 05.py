def inverter_vetor(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverter_vetor(vetor, inicio + 1, fim - 1)

meu_vetor = [9, 12, 34, 23, 58]
print("Vetor original:", meu_vetor)

inverter_vetor(meu_vetor, 0, len(meu_vetor) - 1)

print("Vetor invertido:", meu_vetor)
