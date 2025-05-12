import random
a=random.randint(1,10)
print(a)
vidas=3
while vidas>0:
    i=int(input("Ingrese un numero (1-10): "))
    if i==a:
        print("Ganaste!!!!!!!!!!!!!!!!!!!!")
        break
    else:
        vidas-=1
        print(f"Incorrecto, te quedan {vidas} vidas")
    if vidas<1:
        print(f"Perdiste sanguango, el numero era {a}")