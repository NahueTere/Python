min=0
for x in range (7):
    minutos=int(input("cuantos minutos entreno hoy: "))
    min+=minutos
pro=min/7
if pro >=30:
    print (f"muy bien venis entrenando un promedio de {pro} minutos diarios.")
else:
    print (f"que mal, tenes que aumentar el entrenamiento diario, solo entrenas {pro} minutos diarios.")