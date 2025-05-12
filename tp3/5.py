num=int(input(": "))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        primo=False
    else:
        primo=True
if primo:
    print("Es primo")
else:
    print("no es primo")
