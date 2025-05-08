d=int(input("que dia es?"))
m=int(input("que mes es?"))
a=int(input("que año es? (>=2000)"))
if d>0 and d<30:
    print("Mañana es",d+1,m,a)
elif m>0 and m<12:
    print("Mañana es",1,m+1,a)
else:
    print("Mañana es",1,1,a+1)