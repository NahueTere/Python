pre=int(input("Ingrese presupuesto: "))
precio=0
while precio<=pre:
    precio+=int(input("Cuanto gasto en esta accion: "))
print(f"Excediste el presupuesto (${pre}), gasto total: (${precio})")