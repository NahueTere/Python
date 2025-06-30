n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)


print("Arreglo rotado a la derecha:")
print(arr[::-1])
