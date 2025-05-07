v1 = int(input("Velocidad del movil 1 (km/h): "))
v2 = int(input("Velocidad del movil 2 (km/h): "))
d = int(input("Distancia entre ellos (km): "))
if v1>0 and v2>0:
    t=d/(v1+v2)
    print("impactaran en ",t, "horas")
else:
    print("Error")