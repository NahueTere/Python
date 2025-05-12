def primo(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False 
    return True
c=0
for i in range(2,1001):
    if primo(i):
        c+=1
print(c)