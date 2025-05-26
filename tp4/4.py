aprobados=0
desaprobados= 0
for x in range (10):
    nota=int(input("nota del alumno: "))
    if nota >=7:
        aprobados+=1
    elif nota <7:
        desaprobados+=1
print (f"en total hubo {aprobados} alumnos aprobados y {desaprobados} desaprobados. ")
