n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

producto = 1
for num in arr:
    producto *= num

print("Producto de todos los elementos:", producto)
