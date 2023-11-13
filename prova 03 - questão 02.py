# Faça um programa que converta números na base 2 (com até 5 algarismos) para seus valores correspondentes na base 10. 
# A conversão dos números deverá ser feita por uma função.

def validando_digitos(num_binario):
    return all(digito == "0" or digito == "1" for digito in num_binario)

def conversão_decimal(num_binario): 
    if not validando_digitos(num_binario):
        print("Entrada inválida! O programa aceita somente números na base binária.")
        return None
    
    if len(num_binario) > 5:
        print("Entrada inválida! O programa só aceita números com até 5 algarismos.")
        return None

    decimal = 0
    tamanho = len(num_binario)

    for i in range(tamanho):
        digito = int(num_binario[tamanho - 1 - i])
        decimal += digito * (2 ** i)

    return decimal

print("=-" * 20)
num_binario = input("Insira um valor binário para ser convertido: ")
resultado_decimal = conversão_decimal(num_binario)

print("=-" * 20)
print(f"> O número binário {num_binario} em decimal é {resultado_decimal}.")