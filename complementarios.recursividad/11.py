par=0
impar=0
for i in range(1,11):
    num=int(input("numero: "))
    if num%2==0:
        par+=1
    else:
        impar+=1
print(f"Hay {par} numeros pares")
print(f"Hay {impar} numeros impares")