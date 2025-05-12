c="pedrito"

attempt=3
while attempt>0:
    i=input("Ingrese contraseña: ")
    if i==c:
        print("Acceso permitido")
        break
    else:
        attempt-=1
        print(f"Incorrecto, te quedan {attempt} intentos")
    if attempt<1:
        print(f"Acceso denegado")