from utilidades.validadores import validar_cadena_no_vacia, validar_numero_positivo

class Ingrediente:
    """
    Entidad que representa la materia prima unitaria del restaurante.
    """
    def __init__(self, nombre: str, unidad_medida: str, costo_por_unidad: float):
        self._nombre = validar_cadena_no_vacia(nombre, "nombre del ingrediente")
        self._unidad_medida = validar_cadena_no_vacia(unidad_medida, "unidad de medida")
        self._costo_por_unidad = validar_numero_positivo(costo_por_unidad, "costo por unidad")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def unidad_medida(self) -> str:
        return self._unidad_medida

    def __str__(self) -> str:
        return f"{self._nombre} ({self._unidad_medida})"