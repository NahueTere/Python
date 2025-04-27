sueldo= int(input("sueldo: "))
if sueldo < 1000:
    sueldo = sueldo*1.15
    print(f"${round(sueldo)}")
else:
    print(f"${round(sueldo)}")