N = int(input("Cantidad de elementos: "))
A = []

for i in range(N):
    num = int(input(f"Elemento {i}: "))
    A.append(num)

A.sort(reverse=True)

print("Vector ordenado descendentemente:")
print(A)
