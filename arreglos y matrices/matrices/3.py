m = int(input("Años: "))
n = int(input("Sucursales: "))

v = []
for i in range(m):
    fila = []
    for j in range(n):
        x = float(input(f"Año {i+1}, Sucursal {j+1}: "))
        fila.append(x)
    v.append(fila)

s = [0] * n
for i in range(m):
    for j in range(n):
        s[j] += v[i][j]

max_s = s.index(max(s)) + 1

p = []
for i in range(m):
    prom = sum(v[i]) / n
    p.append(prom)

max_a = p.index(max(p)) + 1

print(f"\nSucursal que más vendió: {max_s}")
print("Promedios por año:")
for i in range(m):
    print(f"Año {i+1}: {p[i]:.2f}")
print(f"Año con mayor promedio: {max_a}")