num = int(input("num: "))
v = int(input("v: "))
if num==1:
    val=100*v
elif num==2:
    val=100**v
elif num==3:
    val=100/v
else:
    val=0
print(val)