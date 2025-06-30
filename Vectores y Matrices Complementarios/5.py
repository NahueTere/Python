N = int(input("Cantidad de elementos: "))
A = []

for i in range(N):
    num = int(input(f"Elemento {i}: "))
    A.append(num)

valor = int(input("Valor a buscar: "))

pos = -1
for i in range(N):
    if A[i] == valor:
        pos = i
        break

if pos != -1:
    print(f"Valor encontrado en la posición {pos}.")
else:
    print("Valor no encontrado.")

