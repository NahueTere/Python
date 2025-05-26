diacaluroso=0
muycaluroso= 0
print ("semana calurosa")
for x in range (7):
    grados= int(input("cuantos grados hubo hoy? "))
    if grados>30:
        muycaluroso+=1
        diacaluroso+=grados
    elif grados <=30:
        diacaluroso+=grados
pro= diacaluroso/7
print (f"en total hubo un promedio de {pro} grados semanales")
print (f"de 7 dias en la semana {muycaluroso} dias superaron los 30 grados")
