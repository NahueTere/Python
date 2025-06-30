N = int(input("Cantidad de elementos: "))
A = []

for i in range(N):
    num = int(input(f"Elemento {i}: "))
    A.append(num)

A.sort()

print("Vector ordenado ascendentemente:")
print(A)
nuevo = int(input("Nuevo elemento: "))
A.append(nuevo)
A.sort()
print(A)