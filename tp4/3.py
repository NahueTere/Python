agua= 0
for x in range (7):
    vasos=int(input("cuanta vasos de agua tomo hoy: "))
    agua+=vasos
agua= agua/7
if agua<8:
    print ("cuidado, esta tomando menos de 8 vasos de agua semanal, intente aumentarlo")
elif agua>= 8:
    print (f"muy bien, esta semana tomo un promedio diario de {agua} vasos de agua")