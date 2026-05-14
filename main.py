# main.py
# main.py
from modelos.actores.cliente import Cliente
from modelos.actores.cajero import Cajero
from modelos.catalogo.ingrediente import Ingrediente
from modelos.catalogo.prod_preparado import ProductoPreparado
from modelos.catalogo.prod_comercial import ProductoComercial
from servicios.gestor_inventario import GestorInventario
from servicios.pedido import Pedido

def main():
    print("=========================================")
    print("  🍔 SISTEMA DE GESTIÓN DE RESTAURANTE  ")
    print("=========================================")

    """
    =======================================================================
    NOTA PARA EL DOCENTE:
    Para efectos de esta demostración y agilizar las pruebas del MVP,
    los datos maestros (Inventario, Recetas y Catálogo base) se encuentran
    pre-cargados (hardcoded).
    En una futura iteración, estos datos provendrían de una base de datos.
    El flujo transaccional (Registro de actores y Pedidos) es 100% dinámico.
    =======================================================================
    """

    # --- 1. CARGA DE DATOS MAESTROS (Fijos) ---
    bodega = GestorInventario()
    pan = Ingrediente("Pan de Hamburguesa", "Unidad", 500)
    carne = Ingrediente("Carne de Res", "Gramos", 15)
    queso = Ingrediente("Queso Cheddar", "Tajada", 300)

    bodega.agregar_ingrediente(pan, 50)
    bodega.agregar_ingrediente(carne, 5000)
    bodega.agregar_ingrediente(queso, 20)

    hamburguesa = ProductoPreparado("Hamburguesa Sencilla", 15000, {pan: 1, carne: 150, queso: 1})
    gaseosa = ProductoComercial("Gaseosa Cola 400ml", 4000)

    # Diccionario para manejar el menú dinámicamente
    menu_disponible = {
        "1": hamburguesa,
        "2": gaseosa
    }

    # --- 2. OPERACIÓN DIARIA (Dinámica e interactiva) ---
    print("\n[APERTURA DE CAJA]")
    cajero_turno = Cajero("1122", "Andrea Gomez", "EMP-01", "mañana")
    print(f"✅ Caja abierta por: {cajero_turno.nombre}")

    print("\n[LLEGADA DE CLIENTE]")
    # Aquí podrías usar la función interactiva registrar_cliente_interactivo() que hicimos antes
    # Por ahora lo dejamos semidinámico para la prueba del menú
    # Bucle infinito que solo se rompe si los datos son correctos
    while True:
        try:
            id_cliente = input("Ingrese ID Cliente: ")
            nombre_cliente = input("Ingrese Nombre (solo letras): ")
            tel_cliente = input("Ingrese Teléfono (ej: +57311...): ")

            # Intenta crear el objeto. Si un validador falla, salta al 'except'
            cliente_actual = Cliente(id_cliente, nombre_cliente, tel_cliente)

            print(f"✅ Cliente '{cliente_actual.nombre}' registrado con éxito.")
            break  # Sale del bucle porque no hubo errores

        except ValueError as e:
            # Atrapa el error, informa al usuario y repite el bucle
            print(f"❌ Error de ingreso: {e}")
            print("🔄 Inténtelo nuevamente.\n")

    # --- 3. CREACIÓN DEL PEDIDO DINÁMICO ---
    pedido_actual = Pedido(numero_pedido=101, cliente=cliente_actual, cajero=cajero_turno)

    # Bucle infinito para la toma de pedidos
    while True:
        try:
            print("\nOpciones del Menú:")
            print(f"1. {hamburguesa.nombre} - ${hamburguesa.precio_base}")
            print(f"2. {gaseosa.nombre} - ${gaseosa.precio_base}")
            print("0. Finalizar y Pagar")
            print("9. Cancelar Pedido")

            # .strip() elimina espacios accidentales al inicio o final
            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "0":
                # Control de error: Evitar procesar un pedido vacío
                # Accedemos a la longitud de la lista de productos (idealmente con un método del Pedido)
                if len(pedido_actual._productos) == 0:
                    print("⚠️ Acción denegada: El carrito está vacío. Agregue productos antes de pagar.")
                    continue # Vuelve al inicio del bucle
                break # Sale del bucle para procesar el pago

            elif opcion == "9":
                # Control de UX: Abortar la operación limpiamente
                print("🚫 Pedido cancelado por el cajero. No se descontará inventario.")
                return # Termina la ejecución de main() prematuramente

            elif opcion in menu_disponible:
                producto_seleccionado = menu_disponible[opcion]
                pedido_actual.agregar_producto(producto_seleccionado)

            else:
                # Control de error: Letras o números fuera del catálogo
                print(f"❌ Error: La opción '{opcion}' no es válida. Digite un número del menú.")

        except Exception as e:
            # Control de fallos del sistema o interrupciones inesperadas
            print(f"❌ Error crítico en el sistema de pedidos: {e}")
            print("🔄 Recuperando la sesión...")

    # --- 4. PROCESAMIENTO Y CIERRE ---
    print("\n--- ⚙️ PROCESANDO TRANSACCIÓN ---")
    try:
        pedido_actual.procesar_pedido(bodega)
        print(pedido_actual.generar_factura())

        print("\n--- 📦 ESTADO DE BODEGA POST-VENTA ---")
        print(bodega.mostrar_inventario_actual())
    except ValueError as e:
        print(f"\n❌ Error crítico en la transacción: {e}")

if __name__ == "__main__":
    main()