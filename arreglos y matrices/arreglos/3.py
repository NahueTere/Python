VEC = [] 
print("Ingrese número de elementos del vector")
N = int( input())

if 1 <= N and N <= 200:
    for i in range(1,N+1):
        elemento = int( input(f"Ingrese Entero {i}: "))
        VEC.append(elemento)
        

lista_nueva = [] 
for elemento in VEC:

    if elemento not in lista_nueva:
        lista_nueva.append(elemento) 

print(lista_nueva)