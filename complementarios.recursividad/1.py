pares=0
print("ingrese 100 numeros enteros")
for i in range(1,101):
    n=int(input(f"num {i}:"))
    if n%2==0:
        pares+=1 
print(f"Hay {pares} numero pares")