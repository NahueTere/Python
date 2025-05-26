print("0=Fin")
mayor=0
total=0
while True:
    donado=int(input("Donado: "))
    if donado>mayor:
        mayor=donado
    total+=donado
    if donado==0:
        break
print(f"Total donado ${total} y la mayor donacion fue de ${mayor}")