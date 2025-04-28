saldo=1000
rtr=int(input("monto a retirar: "))
if rtr<=saldo:
    print ("se completo la transaccion")
    print(f"Saldo disponible ${saldo-rtr}")
elif rtr>=saldo:
    print("saldo insuficiente")
    