from core.abstract_producto import Producto

class ProductoPreparado(Producto):
    """
    Producto que se ensambla en cocina usando el inventario (ej. Hamburguesa).
    """
    def __init__(self, nombre: str, precio_base: float, receta: dict):
        super().__init__(nombre, precio_base)

        # Validamos que la receta exista y sea un diccionario
        if not isinstance(receta, dict) or not receta:
            raise ValueError(f"El producto preparado '{self._nombre}' DEBE tener una receta válida.")

        self._receta = receta

    @property
    def receta(self) -> dict:
        return self._receta

    def calcular_precio_final(self) -> float:
        # El restaurante de comidas rápidas define que el precio base ya incluye
        # el costo de los ingredientes y el margen de ganancia. No suma IVA.
        return self.precio_base

    def mostrar_receta(self) -> str:
        """Método de utilidad para ver de qué está hecho este producto."""
        detalle = f"Receta de {self.nombre}:\n"
        for ingrediente, cantidad in self._receta.items():
            detalle += f"  - {cantidad} {ingrediente.unidad_medida} de {ingrediente.nombre}\n"
        return detalle