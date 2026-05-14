# main.py
from modelos.actores.cliente import Cliente
from modelos.actores.cajero import Cajero

def main():
    print("=== SIMULADOR DE RESTAURANTE ===")

    print("\n--- 1. Prueba de instanciación EXITOSA ---")
    try:
        cliente_1 = Cliente(identificacion="1053001122", nombre="Johan Marcelo", telefono="3001234567")
        cajero_1 = Cajero(identificacion="99887766", nombre="Laura Perez", codigo_empleado="EMP-01", turno="Tarde")
        print("✅", cliente_1.mostrar_informacion())
        print("✅", cajero_1.mostrar_informacion())
    except ValueError as error:
        print(f"❌ Error inesperado: {error}")
    print("\n--- 2. Prueba de validadores (Errores provocados) ---")

    # Prueba A: Nombre con números
    try:
        cliente_falso = Cliente(identificacion="111", nombre="Juan123", telefono="3000000000")
    except ValueError as error:
        print(f"🛡️  Validación activada (Nombre incorrecto): {error}")
    # Prueba B: Turno inválido
    try:
        cajero_falso = Cajero(identificacion="222", nombre="Carlos", codigo_empleado="EMP-02", turno="Madrugada")
    except ValueError as error:
        print(f"🛡️  Validación activada (Turno incorrecto): {error}")

if __name__ == "__main__":
    main()