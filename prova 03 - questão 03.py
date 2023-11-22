def calcular_nota_final(nota_mensal1, nota_mensal2, nota_mensal3, nota_mensal4, nota_final):
    notas_mensais = [nota_mensal1, nota_mensal2, nota_mensal3, nota_mensal4]
    notas_mensais.sort(reverse=True)
    
    nota_final_calculada = sum(notas_mensais[:3]) + nota_final
    return nota_final_calculada

def atribuir_conceito(nota_final):
    if 90 <= nota_final <= 100:
        return 'A'
    elif 80 <= nota_final <= 89:
        return 'B'
    elif 70 <= nota_final <= 79:
        return 'C'
    elif 60 <= nota_final <= 69:
        return 'D'
    elif 40 <= nota_final <= 59:
        return 'E'
    else:
        return 'F'

def main():
    while True:
        numero_aluno = int(input("Número do aluno (negativo para encerrar): "))
        
        if numero_aluno < 0:
            break
        
        nota_mensal1 = float(input("1° Nota mensal: "))
        nota_mensal2 = float(input("2° Nota mensal: "))
        nota_mensal3 = float(input("3° Nota mensal: "))
        nota_mensal4 = float(input("4° Nota mensal: "))
        nota_final = float(input("Nota final: "))
        
        nota_final_aluno = calcular_nota_final(nota_mensal1, nota_mensal2, nota_mensal3, nota_mensal4, nota_final)
        conceito_aluno = atribuir_conceito(nota_final_aluno)
        print("=-"*19)
        print(f" > Aluno {numero_aluno} \n > Nota Final: {nota_final_aluno} \n > Conceito: {conceito_aluno}")

if __name__ == "__main__":
    main()
