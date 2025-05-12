numero=int(input("Ingrese el numero: "))
while numero>0:
    suma=0
    for i in range(1,numero+1):
        if numero%i==0:
            suma+=i
    print(f"La suma de los dividores de {numero} es {suma}")
    numero=int(input("Ingrese otro numero: "))