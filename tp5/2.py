n = int(input("Número entero positivo: "))
suma = 0

while n > 0:
    suma += n % 10
    n //= 10

print("Suma de los dígitos:", suma)
