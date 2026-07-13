
import sys
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_menu():
    servicio = Restaurante()

    while True:
        print("========================================")
        print("        SISTEMA DE RESTAURANTE")
        print("========================================")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("----------------------------------------")
        print("4. Registrar cliente")
        print("5. Listar clientes")
        print("6. Buscar cliente")
        print("----------------------------------------")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto: ")
                precio = float(input("Precio del producto: "))
                disponible_input = input("¿Está disponible? (s/n): ").strip().lower()
                disponible = disponible_input != 'n'

                nuevo_producto = Producto(nombre, categoria, precio, disponible)
                servicio.registrar_producto(nuevo_producto)
                print("Producto registrado con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            servicio.listar_productos()
            print()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            encontrado = servicio.buscar_producto(nombre)
            if encontrado:
                encontrado.mostrar_informacion()
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del cliente: ").strip()
            correo = input("Correo del cliente: ").strip()
            id_cliente = input("ID/Cédula del cliente: ").strip()

            if not nombre or not correo or not id_cliente:
                print("Error: Todos los datos del cliente son obligatorios.")
                continue

            nuevo_cliente = Cliente(nombre, correo, id_cliente)
            servicio.registrar_cliente(nuevo_cliente)
            print("Cliente registrado con éxito.")

        elif opcion == "5":
            print("\n--- Lista de Clientes ---")
            servicio.listar_clientes()
            print()

        elif opcion == "6":
            id_cliente = input("Ingrese el ID del cliente a buscar: ")
            encontrado = servicio.buscar_cliente(id_cliente)
            if encontrado:
                encontrado.mostrar_informacion()
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()
