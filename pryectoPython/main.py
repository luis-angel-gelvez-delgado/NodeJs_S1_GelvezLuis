# main.py
from gastos_manager import registrar_gasto, listar_gastos, calcular_total
from reportes import generar_reporte

def menu_principal():
    while True:
        print("""
=============================================
         Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Salir
=============================================
""")
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            listar_gastos()
        elif opcion == "3":
            menu_totales()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            salir = input("¿Desea salir del programa? (S/N): ").strip().upper()
            if salir == "S":
                print("Gracias por usar el simulador.")
                break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_totales():
    while True:
        print("""
=============================================
          Calcular Total de Gastos
=============================================
1. Total diario
2. Total semanal
3. Total mensual
4. Regresar al menú principal
=============================================
""")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            calcular_total("diario")
        elif opcion == "2":
            calcular_total("semanal")
        elif opcion == "3":
            calcular_total("mensual")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_reportes():
    while True:
        print("""
=============================================
           Generar Reporte de Gastos
=============================================
1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar al menú principal
=============================================
""")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            generar_reporte("diario")
        elif opcion == "2":
            generar_reporte("semanal")
        elif opcion == "3":
            generar_reporte("mensual")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
