n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

cont_pares = 0
for num in arr:
    if num % 2 == 0:
        cont_pares += 1

print("Cantidad de elementos pares:", cont_pares)
