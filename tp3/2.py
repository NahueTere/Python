edad=1
n=0
ad=0
a=0

while edad>0:
    edad=int(input("ingrese edad: "))
    if edad<14 and edad>0:
        n+=1
    elif edad<16 and edad>13:
        ad+=1
    elif edad>17:
        a+=1
    else: 
        exit
print(f"Hay {n} niños, {ad} adolescentes y {a} adultos")