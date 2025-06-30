# Ingreso del vector de caracteres
n = int(input("¿Cuántos caracteres querés ingresar?: "))
v = []

for i in range(n):
    c = input(f"Caracter {i + 1}: ")
    v.append(c)



# Mostrar resultado
print("Vector invertido:")
print(v[::-1])
