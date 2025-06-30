actividad = []
for i in range(7):
    minutos = int(input(f"Minutos día {i + 1}: "))
    actividad.append(minutos)

promedio = sum(actividad) / 7
maximo = max(actividad)
minimo = min(actividad)
dia_max = actividad.index(maximo) + 1
dia_min = actividad.index(minimo) + 1

print("Promedio semanal:", promedio)
print("Día con más actividad:", dia_max)
print("Día con menos actividad:", dia_min)
