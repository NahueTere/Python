tanque= 0
carga= int(input("cuanto combustible va a cargar? tiene que hacer 50 km: "))
tanque+= carga
recorrido = tanque/0.07
if recorrido >50 :
   print ("muy bien, te alcanzo" ) 
elif recorrido <50:
   print ("no te dio la nafta")