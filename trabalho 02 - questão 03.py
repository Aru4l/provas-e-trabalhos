def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

valor_m = 3
valor_n = 2

resultado = ackermann(valor_m, valor_n)
print(f"A({valor_m}, {valor_n}) = {resultado}")