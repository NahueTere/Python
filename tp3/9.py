t=0
menor0=0
mas30=0
while t>-100:
    t=int(input(": "))
    if t<0 and t>-100:
        menor0+=1
    elif t>=30:
        mas30+=1
print(f"hay {menor0} temperaturas menores a 0 y {mas30} mayores o iguales a 30")