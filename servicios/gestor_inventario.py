from modelos.catalogo.ingrediente import Ingrediente
from utilidades.validadores import validar_numero_positivo

class GestorInventario:
    """
    Servicio encargado de controlar el stock de la materia prima.
    Sigue el principio de Responsabilidad Única (SRP).
    """
    def __init__(self):
        # El inventario será un diccionario: {objeto_ingrediente: cantidad_flotante}
        self._stock = {}

    def agregar_ingrediente(self, ingrediente: Ingrediente, cantidad_inicial: float):
        """Registra un nuevo ingrediente en la bodega."""
        cantidad_valida = validar_numero_positivo(cantidad_inicial, "cantidad inicial")
        if ingrediente not in self._stock:
            self._stock[ingrediente] = cantidad_valida
        else:
            self._stock[ingrediente] += cantidad_valida

    def consumir_stock(self, ingrediente: Ingrediente, cantidad_requerida: float):
        """Descuenta material del inventario si hay suficiente."""
        cantidad_valida = validar_numero_positivo(cantidad_requerida, "cantidad requerida", permite_cero=False)

        if ingrediente not in self._stock:
            raise ValueError(f"El ingrediente '{ingrediente.nombre}' no existe en el inventario.")

        if self._stock[ingrediente] < cantidad_valida:
            raise ValueError(f"Stock insuficiente de {ingrediente.nombre}."f"Disponible: {self._stock[ingrediente]}, Requerido: {cantidad_valida}")
        # Descuento exitoso
        self._stock[ingrediente] -= cantidad_valida

    def generar_reporte_compras(self, umbral_minimo: float = 10.0) -> list:
        """Retorna una lista de ingredientes que están por debajo del umbral de seguridad."""
        alerta_compras = []
        for ingrediente, cantidad in self._stock.items():
            if cantidad <= umbral_minimo:
                alerta_compras.append(f"COMPRAR: {ingrediente.nombre} (Quedan {cantidad} {ingrediente.unidad_medida})")
        return alerta_compras

    def mostrar_inventario_actual(self) -> str:
        """Devuelve un string con el estado actual de la bodega."""
        if not self._stock:
            return "El inventario está vacío."
        reporte = "--- BODEGA ACTUAL ---\n"
        for ingrediente, cantidad in self._stock.items():
            reporte += f"- {ingrediente.nombre}: {cantidad} {ingrediente.unidad_medida}\n"
        return reporte