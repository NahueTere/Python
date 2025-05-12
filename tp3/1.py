notas=[]
for x in range(1,6):
    nota=int(input("ingrese la nota: "))
    notas.append(nota)
if sum(notas)/5>=7:
    print("En promedio han aprobado")
else:
    print("En promedio no ha aprobado")