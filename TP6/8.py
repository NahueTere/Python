n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

buscar = int(input("Número a buscar: "))

if buscar in arr:
    print("Índice de la primera aparición:", arr.index(buscar))
else:
    print("El número no está en el arreglo.")
