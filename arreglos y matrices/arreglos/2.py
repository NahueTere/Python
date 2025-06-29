Suma = 0
Media = 0.0
C = 0
Temp = [] 
print("Ingrese cantidad de Temperaturas: ")
N = int( input())
for i in range(N):
    temperatura = float( input(f"Ingrese Temperatura {i+1}: "))
    Temp.append(temperatura)
    Suma = Suma + Temp[i]
Media = Suma / N 
for temps in Temp: 
    if temps >= Media:
        C = C + 1

print ("La media es ", Media)
print ("Total de temperaturas mayores o iguales a la media es", C)