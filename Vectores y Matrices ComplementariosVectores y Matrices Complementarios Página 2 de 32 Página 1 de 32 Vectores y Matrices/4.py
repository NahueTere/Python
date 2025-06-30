vector = []
MAX = 10

while True:
    print("\nMENÚ")
    print("1. Añadir un elemento")
    print("2. Eliminar un elemento")
    print("3. Listar el contenido")
    print("4. Contar apariciones de un número")
    print("5. Calcular media y máximo")
    print("0. Terminar")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        if len(vector) < MAX:
            num = int(input("Ingresá un número: "))
            vector.append(num)
            print("Elemento añadido.")
        else:
            print("El vector está lleno.")

    elif opcion == "2":
        if vector:
            num = int(input("Número a eliminar: "))
            if num in vector:
                vector.remove(num)
                print("Elemento eliminado.")
            else:
                print("Ese número no está en el vector.")
        else:
            print("El vector está vacío.")

    elif opcion == "3":
        print("Contenido del vector:", vector)

    elif opcion == "4":
        num = int(input("Número a contar: "))
        cantidad = vector.count(num)
        print(f"Aparece {cantidad} vez/veces.")

    elif opcion == "5":
        if vector:
            media = sum(vector) / len(vector)
            maximo = max(vector)
            print(f"Media: {media}")
            print(f"Máximo: {maximo}")
        else:
            print("El vector está vacío.")

    elif opcion == "0":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida.")
