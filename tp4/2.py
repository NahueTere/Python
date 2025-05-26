cantidad=int(input("Total de cargas: "))
litros=0
for i in range(1,cantidad+1):
    carga=int(input("Cuanto litros cargo?: "))
    if carga<5:
        print("sospecha de error o carga minima")
    litros+=carga
pro=litros/cantidad
print(f"En total se han realizado {cantidad} cargas")
print(f"En total se cargaron {litros} litros")
print(f"El promedio de litros por carga es {pro}")