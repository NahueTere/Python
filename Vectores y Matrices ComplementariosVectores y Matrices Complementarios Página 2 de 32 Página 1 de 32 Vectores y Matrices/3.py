B = 100 * [True]
N = []

for i in range(1, 101):
    N.append(i)

B[0] = False

for i in range(1, 99):
    for j in range(i + 1, 100):
        if N[j] % N[i] == 0:
            B[j] = False

primos = []

for i in range(100):
    if B[i]:
        primos.append(N[i])

print(primos)
