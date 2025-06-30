n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

sin_duplicados = []

for num in arr:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Arreglo sin duplicados:")
print(sin_duplicados)
