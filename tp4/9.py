presu=20000
print ("tiene 20.000 pesos de presupuesto")
while True:
    compra=int(input("cuanto gasto: "))
    presu-= compra
    if presu <= 0:
        print ("ya no te queda mas dinero")
        break
    elif presu >0:
        print (f"que sigue? aun te quedan {presu} pesos ")
    