par=0
for i in range(1,6):
    num=int(input(": "))
    if num%2==0:
        par+=1
if par>0:
    print(f"hay al menos un numero par ({par})")
else:
    print("No hay numeros pares")