total = ventas_altas = 0

while True:
    seguir = input("¿Registrar venta? (s/n): ").lower()
    if seguir != "s":
        break
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario: "))
    subtotal = cantidad * precio
    total += subtotal
    if subtotal > 1000:
        ventas_altas += 1

print("Total vendido:", total)
print("Ventas mayores a $1000:", ventas_altas)
