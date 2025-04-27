año= int(input("año:"))
if (año%4==0 and año%100!=0) or año%400==0:
    print("es bisiesto")
else:
    print("no es bisiesto")