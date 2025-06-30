n = int(input("Cantidad de elementos: "))
arr = []
arr_or = []

for i in range(n):
    num = int(input(f"Elemento {i + 1}: "))
    arr.append(num)
    arr_or.append(num)
arr_or.sort()

if arr==arr_or:
        print("El arreglo esta ordenado")
else:
        print("El arreglo no esta ordenado")
