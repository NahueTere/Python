n = int(input("Cantidad de elementos: "))
arr = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)

mayor = max(arr)
segundo_mayor = 0

for num in arr:
    if num != mayor and num > segundo_mayor:
        segundo_mayor = num

else:
    print("El segundo mayor elemento es:", segundo_mayor)
