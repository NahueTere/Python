clave = "1234"
intentos = 0
acceso = False

while intentos < 3:
    entrada = input("Ingresá la contraseña: ")
    if entrada == clave:
        acceso = True
        break
    intentos += 1

if acceso:
    print("Acceso concedido.")
else:
    print("Acceso bloqueado.")
