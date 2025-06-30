print("Ingresá los 3 elementos del vector A:")
a = []
for i in range(3):
    val = float(input(f"  A[{i}]: "))
    a.append(val)

print("Ingresá los 3 elementos del vector B:")
b = []
for i in range(3):
    val = float(input(f"  B[{i}]: "))
    b.append(val)

p_esc = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

p_vec = [
    a[1]*b[2] - a[2]*b[1],
    a[2]*b[0] - a[0]*b[2],
    a[0]*b[1] - a[1]*b[0]
]

print("\nResultado:")
print(f"Producto escalar: {p_esc}")
print(f"Producto vectorial: {p_vec}")
