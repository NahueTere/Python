print ("Ingrese la cantidad de empleados:")
ce = int( input())

i = 1
smayor = 0.0 

print("Ingrese los sueldos: ")
while i <= ce :
    sueldo = float( input("Ingrese sueldo {0}: ".format(i)))
    if sueldo > smayor :
        smayor = sueldo
        c = i
        i = i + 1

print ("El empleado numero ", c, "tiene el mayor sueldo que es:", smayor)