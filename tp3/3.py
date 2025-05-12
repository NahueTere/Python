precio=0
p=1
while p>0:
    p=int(input("precio: "))
    precio+=p
if precio>10000:
    precio=precio*0.9
print(f"Total a pagar: ${precio}")
