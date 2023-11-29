import math

def calcular_cosseno(x):
    radiano = math.radians(x)
    cos_x = 1  

    for n in range(1, 16):  
        termo = ((-1) ** n) * (radiano ** (2 * n)) / math.factorial(2 * n)
        cos_x += termo

    return cos_x

for x in range(0, 64):
    x /= 10.0  
    resultado_cosseno = calcular_cosseno(x)
    print(f"x = {x:.1f}, cos(x) = {resultado_cosseno:.4f}")
