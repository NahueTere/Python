num=int(input("Ingrese un numero: "))
if num<10 and num>0:
    if num%2==0:
        print("Es par")
    else:
        print("Es impar")
else:
    print("debe ser entre 0 y 10")
