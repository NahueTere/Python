A = [
    [1, 3, 3],
    [2, 5, 6],
    [3, 6, 9]
]

es_simetrica = True
n = len(A)

for i in range(n):
    for j in range(i + 1, n):  # Parte superior
        if A[i][j] != A[j][i]:
            es_simetrica = False
            break

if es_simetrica:
    print("La matriz es simétrica.")
else:
    print("La matriz NO es simétrica.")