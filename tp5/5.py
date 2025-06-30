total = cantidad_items = 0

while True:
    seguir = input("¿Agregar producto? (s/n): ").lower()
    if seguir != "s":
        break
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))
    total += precio * cantidad
    cantidad_items += cantidad

print("Total acumulado:", total)
print("Cantidad total de ítems:", cantidad_items)
