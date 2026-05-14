from modelos.actores.cliente import Cliente
from modelos.actores.cajero import Cajero
from core.abstract_producto import Producto
from modelos.catalogo.prod_preparado import ProductoPreparado
from servicios.gestor_inventario import GestorInventario

class Pedido:
    """
    Clase que representa la transacción principal del restaurante.
    Vincula a los actores con los productos y actualiza el estado del negocio.
    """
    def __init__(self, numero_pedido: int, cliente: Cliente, cajero: Cajero):
        self._numero_pedido = numero_pedido
        self._cliente = cliente
        self._cajero = cajero
        self._productos = []  # Lista vacía que se llenará con objetos Producto
        self._estado = "Abierto" # Estados: Abierto, Procesado

    @property
    def numero_pedido(self) -> int:
        return self._numero_pedido

    @property
    def total(self) -> float:
        return self.calcular_total()

    def agregar_producto(self, producto: Producto):
        """Añade un artículo al carrito del cliente."""
        self._productos.append(producto)
        print(f"🛒 Añadido: {producto.nombre} al pedido #{self._numero_pedido}")

    def calcular_total(self) -> float:
        """Recorre la lista de productos y suma sus precios finales."""
        suma_total = 0.0
        for prod in self._productos:
            suma_total += prod.calcular_precio_final()
        return suma_total

    def procesar_pedido(self, inventario: GestorInventario):
        """
        Confirma la orden, verifica las recetas y descuenta del inventario.
        Si falta un ingrediente, el proceso se detiene y lanza un error.
        """
        if not self._productos:
            raise ValueError("No se puede procesar un pedido sin productos.")

        print(f"\n⚙️ Procesando pedido #{self._numero_pedido}...")

        # Recorremos cada producto comprado
        for producto in self._productos:
            # Si el producto es preparado, leemos su receta y descontamos
            if isinstance(producto, ProductoPreparado):
                for ingrediente, cantidad_necesaria in producto.receta.items():
                    inventario.consumir_stock(ingrediente, cantidad_necesaria)

        self._estado = "Procesado"
        print("✅ Pedido procesado: Ingredientes descontados correctamente.")

    def generar_factura(self) -> str:
        """Genera el ticket de compra final."""
        factura = f"\n{'='*40}\n"
        factura += f"🍔 TICKET DE COMPRA - PEDIDO #{self._numero_pedido} 🍔\n"
        factura += f"{'='*40}\n"
        factura += f"Atiende: {self._cajero.nombre} (Turno {self._cajero.turno})\n"
        factura += f"Cliente: {self._cliente.nombre} | Doc: {self._cliente.identificacion}\n"
        factura += f"{'-'*40}\n"

        for prod in self._productos:
            factura += f"1x {prod.nombre:<25} ${prod.calcular_precio_final():.2f}\n"

        factura += f"{'-'*40}\n"
        factura += f"TOTAL A PAGAR:               ${self.calcular_total():.2f}\n"
        factura += f"ESTADO: {self._estado}\n"
        factura += f"{'='*40}\n"
        return factura