a = 0
b = 1

while a <= 10000:
    print(a, end=" ")
    a, b = b, a + b
