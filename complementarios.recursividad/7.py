primo=True
num = int(input("a: "))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        primo=False 

print(f"{num} es primo?: {primo}")