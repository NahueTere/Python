suma = count = fuera_rango = 0

while True:
    nota = int(input("Ingresá una nota (-1 para salir): "))
    if nota == -1:
        break
    elif 1 <= nota <= 10:
        suma += nota
        count += 1
    else:
        fuera_rango += 1

if count > 0:
    print("Promedio:", suma / count)
else:
    print("No se ingresaron notas válidas.")

print("Notas fuera de rango:", fuera_rango)
