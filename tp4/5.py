stock  =int(input("cuanto stock de pochoclo tenes: "))
stockactual=stock
while stockactual>0:
    venta=int(input("cuantos productos vendiste "))
    if venta==0:
        break
    stockactual-=venta
    if stockactual<=stock*0.1:
        print(f"Tiene menos del 10% de stock, te quedan {stockactual} articulos")
    elif stockactual==0:
        print("Ya vendio todo!")
    else:
        print(f"Te quedan {stockactual} unidades disponibles")
    
    
