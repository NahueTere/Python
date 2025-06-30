n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

print("Elementos únicos:")
for num in arr:
    if arr.count(num) == 1:
        print(num)
