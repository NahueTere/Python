import random
A = [0] * 100
pares = [0] * 100
impares = [0] * 100

for i in range(100):
    A[i] = random.randint(1,1001)

cp = 0  # contador de pares
ci = 0  # contador de impares

for i in range(100):
    if A[i] % 2 == 0:
        pares[cp] = A[i]
        cp += 1
    else:
        impares[ci] = A[i]
        ci += 1

print("Cantidad de pares:", cp)
print("Cantidad de impares:", ci)

if cp > ci:
    print("El vector de pares es más grande.")
elif ci > cp:
    print("El vector de impares es más grande.")
else:
    print("Ambos vectores tienen la misma cantidad de elementos.")
