def decimal_para_binario(decimal):
    if decimal <= 1:
        return str(decimal)
    else:
        resto = decimal % 2
        quociente = decimal // 2
        return decimal_para_binario(quociente) + str(resto)

numero_decimal = 19
numero_binario = decimal_para_binario(numero_decimal)

print(f"> O número binário correspondente a {numero_decimal} é {numero_binario}")