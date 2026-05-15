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
    # se agrega validacion de factura electronica para solicitar datos completos o rapidos de consumidor final
    while True:
        try:
            factura_electronica = input("¿El cliente solicita Factura Electrónica? (S/N): ").strip().upper()

            if factura_electronica == 'S':
                print("--- Ingreso de datos para Facturación Electrónica ---")
                id_cliente = input("Ingrese Cédula/NIT (Solo números): ")
                nombre_cliente = input("Ingrese Nombre Completo: ")
                tel_cliente = input("Ingrese Teléfono: ")
                correo_cliente = input("Ingrese Correo Electrónico: ")

                # Instanciamos con todos los datos
                cliente_actual = Cliente(id_cliente, nombre_cliente, tel_cliente, correo_cliente)

            elif factura_electronica == 'N':
                print("--- Ingreso rápido (Consumidor Final) ---")
                id_cliente = "2222222222" # Código genérico para consumidor final
                nombre_cliente = input("Ingrese Nombre (Para llamar el pedido): ")
                tel_cliente = input("Ingrese Teléfono (Opcional, presione Enter para omitir): ")

                # Si omite el teléfono en pedido rápido, ponemos uno de relleno válido para evitar error
                if not tel_cliente:
                    tel_cliente = "0000000"

                correo_cliente = "No aplica"

                # Instanciamos
                cliente_actual = Cliente(id_cliente, nombre_cliente, tel_cliente, correo_cliente)

            else:
                print("❌ Opción inválida. Por favor digite 'S' o 'N'.")
                continue # Reinicia el ciclo

            print(f"✅ Cliente '{cliente_actual.nombre}' registrado con éxito.")
            break

        except ValueError as e:
            print(f"❌ Error de ingreso: {e}")
            print("🔄 Inténtelo nuevamente.\n")

    # --- 3. CREACIÓN DEL PEDIDO DINÁMICO ---
    pedido_actual = Pedido(numero_pedido=101, cliente=cliente_actual, cajero=cajero_turno)

    print("\n--- 📝 TOMA DE PEDIDO ---")
    while True:
        print("\nOpciones del Menú:")
        print(f"1. {hamburguesa.nombre} - ${hamburguesa.precio_base}")
        print(f"2. {gaseosa.nombre} - ${gaseosa.precio_base}")
        print("0. Finalizar y Pagar")

        opcion = input("\nSeleccione un producto (0-2): ")

        if opcion == "0":
            break
        elif opcion in menu_disponible:
            producto_seleccionado = menu_disponible[opcion]
            pedido_actual.agregar_producto(producto_seleccionado)
        else:
            print("❌ Opción inválida. Intente de nuevo.")

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