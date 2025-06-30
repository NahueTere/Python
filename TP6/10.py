n1 = int(input("Cantidad de elementos del primer arreglo: "))
arr1 = []
for i in range(n1):
    num = int(input(f"Primer arreglo - Elemento {i + 1}: "))
    arr1.append(num)

n2 = int(input("Cantidad de elementos del segundo arreglo: "))
arr2 = []
for i in range(n2):
    num = int(input(f"Segundo arreglo - Elemento {i + 1}: "))
    arr2.append(num)

combinado = arr1 + arr2

print("Arreglo combinado:")
print(combinado)
