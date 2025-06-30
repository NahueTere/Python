animales = []

for i in range(200):
    nombre = input(f"Ingresá el nombre del animal {i + 1}: ")
    animales.append(nombre)

buscado = input("Ingresá el nombre del animal a buscar: ")

if buscado in animales:
    pos = animales.index(buscado)

    if pos > 0:
        print("Animal a la izquierda:", animales[pos - 1])
    else:
        print("No hay animal a la izquierda (es el primero).")

    if pos < 199:
        print("Animal a la derecha:", animales[pos + 1])
    else:
        print("No hay animal a la derecha (es el último).")
else:
    print("Animal no encontrado.")
