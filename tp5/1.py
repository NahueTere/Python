positivos = negativos = ceros = 0

for i in range(20):
    n = int(input(f"Número {i + 1}: "))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
