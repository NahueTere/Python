mayor=-9999
menor=9999
n = int(input("Cuantos numeros?: "))
for i in range(1,n+1):
    num=int(input("Numero: "))
    if num>mayor:
        mayor=num
    elif num<menor:
        menor=num
print(f"El menor numero es: {menor}")
print(f"El mayor numero es: {mayor}")