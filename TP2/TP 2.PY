import random
import string

# ==== FUNCIONES ====

# EJERCICIO 1 – Calculadora de propinas
def propina_calculadora():
    try:
        cuenta = float(input("¿Cuánto fue el total de la cuenta? $"))
        porcentaje = float(input("¿Qué porcentaje querés dejar de propina? %"))
        extra = cuenta * (porcentaje / 100)
        total_final = cuenta + extra
        print(f"Propina sugerida: ${extra:.2f}")
        print(f"Total con propina: ${total_final:.2f}")
    except ValueError:
        print("Ingresaste un valor no válido.")

# EJERCICIO 2 – Conversor de unidades
def convertir_unidades():
    print("\nElija qué desea convertir:")
    print("A. Libras → Kilogramos")
    print("B. Kilómetros → Millas")
    print("C. Celsius → Fahrenheit")
    eleccion = input("Opción (A/B/C): ").strip().upper()

    if eleccion == "A":
        try:
            libras = float(input("Ingrese peso en libras: "))
            kg = libras * 0.453592
            print(f"{libras} lb equivalen a {kg:.2f} kg")
        except ValueError:
            print("Debe ingresar un número.")
    elif eleccion == "B":
        try:
            km = float(input("Ingrese distancia en kilómetros: "))
            mi = km * 0.621371
            print(f"{km} km equivalen a {mi:.2f} millas")
        except ValueError:
            print("Número inválido.")
    elif eleccion == "C":
        try:
            c = float(input("Temperatura en Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C = {f:.2f}°F")
        except ValueError:
            print("Número inválido.")
    else:
        print("Opción incorrecta.")

# EJERCICIO 3 – Gestor de tareas
def tareas_gestor():
    lista = []

    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Añadir tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Borrar tarea")
        print("5. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            nueva = input("Escribí la tarea: ")
            lista.append({"texto": nueva, "hecha": False})
        elif opcion == "2":
            if not lista:
                print("No hay tareas todavía.")
            else:
                for i, t in enumerate(lista):
                    estado = "✔" if t["hecha"] else "✖"
                    print(f"{i + 1}. {t['texto']} [{estado}]")
        elif opcion == "3":
            try:
                num = int(input("Número de tarea hecha: ")) - 1
                if 0 <= num < len(lista):
                    lista[num]["hecha"] = True
                else:
                    print("Tarea inexistente.")
            except ValueError:
                print("Ingresá un número válido.")
        elif opcion == "4":
            try:
                num = int(input("Número de tarea a borrar: ")) - 1
                if 0 <= num < len(lista):
                    lista.pop(num)
                else:
                    print("Tarea inexistente.")
            except ValueError:
                print("Número inválido.")
        elif opcion == "5":
            break
        else:
            print("Elegiste mal, probá de nuevo.")

# EJERCICIO 4 – Control de presupuesto
def gestor_presupuesto():
    try:
        ingresos = float(input("¿Cuánto ganás al mes? $"))
    except ValueError:
        print("Ingresá un número.")
        return

    egresos = {}
    total = 0

    while True:
        categoria = input("Categoría de gasto (o 'fin' para cerrar): ")
        if categoria.lower() == "fin":
            break
        try:
            monto = float(input(f"Gasto en {categoria}: $"))
            egresos[categoria] = egresos.get(categoria, 0) + monto
            total += monto
        except ValueError:
            print("Monto inválido.")

    restante = ingresos - total
    print(f"\nGastos totales: ${total:.2f}")
    print(f"Saldo restante: ${restante:.2f}")
    print("Distribución:")
    for cat, monto in egresos.items():
        porc = (monto / ingresos) * 100
        print(f"- {cat}: ${monto:.2f} ({porc:.1f}%)")

# EJERCICIO 5 – Creador de contraseñas
def crear_password():
    try:
        largo = int(input("¿Cuántos caracteres querés? "))
        if largo <= 0:
            print("Debe ser mayor a cero.")
            return
        base = string.ascii_letters + string.digits + string.punctuation
        clave = "".join(random.choice(base) for _ in range(largo))
        print(f"Tu contraseña segura: {clave}")
    except ValueError:
        print("Eso no es un número.")

# ==== MENÚ PRINCIPAL ====
def principal():
    while True:
        print("\n=== MENÚ ===")
        print("1. Calcular propina")
        print("2. Convertir unidades")
        print("3. Administrar tareas")
        print("4. Presupuesto personal")
        print("5. Generar contraseña")
        print("6. Salir")

        eleccion = input("Elegí una opción (1-6): ")

        if eleccion == "1":
            propina_calculadora()
        elif eleccion == "2":
            convertir_unidades()
        elif eleccion == "3":
            tareas_gestor()
        elif eleccion == "4":
            gestor_presupuesto()
        elif eleccion == "5":
            crear_password()
        elif eleccion == "6":
            print("Gracias por usar el programa. ¡Chau!")
            break
        else:
            print("Opción incorrecta.")

# Ejecutar
principal()
