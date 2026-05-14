from core.abstract_producto import Producto

class ProductoComercial(Producto):
    """
    Producto que no requiere preparación (ej. Gaseosa).
    """
    def __init__(self, nombre: str, precio_base: float):
        super().__init__(nombre, precio_base)

    def calcular_precio_final(self) -> float:
        # Ejemplo: El precio final de un producto comercial podría incluir un IVA del 19%
        precio_con_impuesto = self.precio_base * 1.19
        return round(precio_con_impuesto, 2)