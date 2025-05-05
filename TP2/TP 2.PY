import random
import string

"""EJERCICIO 1"""
def calculadora_propinas():
    total_cuenta = float(input("Ingrese el total de la cuenta ($): "))
    porcentaje = float(input("Ingrese el porcentaje de propina (%): "))
    propina = total_cuenta * porcentaje / 100
    total = total_cuenta + propina
    print(f"Propina: ${propina:.2f}")
    print(f"Total a pagar: ${total:.2f}")

"""EJERCICIO 2"""
def conversor_unidades():
    print("\nOpciones de conversión:")
    print("1. Libras a Kilogramos")
    print("2. Kilómetros a Millas")
    print("3. Celsius a Fahrenheit")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        libras = float(input("Ingrese el peso en libras: "))
        kilogramos = libras * 0.453592
        print(f"{libras} libras son {kilogramos:.2f} kilogramos.")
    elif opcion == "2":
        km = float(input("Ingrese la distancia en kilómetros: "))
        millas = km * 0.621371
        print(f"{km} kilómetros son {millas:.2f} millas.")
    elif opcion == "3":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C son {fahrenheit:.2f}°F.")
    else:
        print("Opción no válida.")

"""EJERCICIO 3"""
def organizador_tareas():
    tareas = []
    while True:
        print("\n--- Organizador de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            tareas.append({"tarea": tarea, "estado": "Pendiente"})
        elif opcion == "2":
            if not tareas:
                print("No hay tareas.")
            else:
                for i, t in enumerate(tareas):
                    print(f"{i+1}. {t['tarea']} [{t['estado']}]")
        elif opcion == "3":
            indice = int(input("Ingrese el número de la tarea completada: ")) - 1
            if 0 <= indice < len(tareas):
                tareas[indice]["estado"] = "Completada"
            else:
                print("Número inválido.")
        elif opcion == "4":
            indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tareas.pop(indice)
            else:
                print("Número inválido.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

"""EJERCICIO 4"""
def calculadora_presupuesto():
    ingresos = float(input("Ingrese sus ingresos totales ($): "))
    gastos = {}
    total_gastos = 0

    while True:
        categoria = input("Ingrese categoría de gasto (o 'fin' para terminar): ")
        if categoria.lower() == "fin":
            break
        monto = float(input(f"Ingrese el gasto en {categoria} ($): "))
        gastos[categoria] = gastos.get(categoria, 0) + monto
        total_gastos += monto

    saldo = ingresos - total_gastos
    print(f"\nTotal gastos: ${total_gastos:.2f}")
    print(f"Saldo disponible: ${saldo:.2f}")
    print("\nEstadísticas de gastos:")
    for categoria, monto in gastos.items():
        porcentaje = (monto / ingresos) * 100
        print(f"- {categoria}: ${monto:.2f} ({porcentaje:.1f}%)")

"""EJERCICIO 5"""
def generador_contraseñas():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Calculadora de Propinas")
        print("2. Conversor de Unidades")
        print("3. Organizador de Tareas")
        print("4. Calculadora de Presupuesto")
        print("5. Generador de Contraseñas Seguras")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            calculadora_propinas()
        elif opcion == "2":
            conversor_unidades()
        elif opcion == "3":
            organizador_tareas()
        elif opcion == "4":
            calculadora_presupuesto()
        elif opcion == "5":
            generador_contraseñas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


menu()