n = int(input("Número a verificar: "))
es_primo = True

if n < 2:
    es_primo = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es primo.")
else:
    print("No es primo.")
