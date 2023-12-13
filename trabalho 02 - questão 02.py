def mdc_euclides(n, m):
    if n == 0:
        return m
    return mdc_euclides(n=m % n, m=n)

numero1 = 60
numero2 = 42

resultado_mdc = mdc_euclides(numero1, numero2)
print(f"O MDC de {numero1} e {numero2} é: {resultado_mdc}")