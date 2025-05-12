pos=0
neg=0
cpos=0
cneg=0
for i in range(1,11):
    num=int(input("Ingrese un numero: "))
    if num<0:
        cneg+=1
        neg+=num
    elif num>0:
        cpos+=1
        pos+=num
print(f"hay {cneg} numeros negativos, un promedio de {neg/cneg}")
print(f"hay {cpos} numeros positivos, un promedio de {pos/cpos}")