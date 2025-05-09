cero=0
c = int(input("ingrese cantidad de numeros: "))
print("Ingrese los numeros")
for i in range(1,c+1):
    n=int(input(f"Numero {i}: "))
    if n == 0:
        cero+=1
print(f"Hay {cero} cero/s")