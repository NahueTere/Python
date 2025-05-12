print("Introduce el capital, el interés y el tiempo apropiados")
c = int(input("Capital: "))
i = int(input("Interes (%): "))
a = int(input("Años: "))

for j in range(1,a+1):
    c = c*(1+i/100)
print(f"Vas a tener ${c}")