n = int(input("Cantidad de elementos en los arreglos: "))
arr1 = []
arr2 = []
suma = []

for i in range(n):
    num = int(input(f"Arreglo 1 - Elemento {i + 1}: "))
    arr1.append(num)

for i in range(n):
    num = int(input(f"Arreglo 2 - Elemento {i + 1}: "))
    arr2.append(num)

for i in range(n):
    suma.append(arr1[i] + arr2[i])

print("Arreglo resultante de la suma:")
print(suma)
