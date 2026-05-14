from abc import ABC, abstractmethod
from utilidades.validadores import validar_cadena_no_vacia, validar_numero_positivo

class Producto(ABC):
    """
    Clase abstracta para los elementos del catálogo.
    """
    def __init__(self, nombre: str, precio_base: float):
        # 'precio_base' es un candidato ideal para un validador de números positivos
        self._nombre = validar_cadena_no_vacia(nombre, "nombre del producto")
        self._precio_base = validar_numero_positivo(precio_base, "precio base")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """
        Método abstracto: Obliga a las clases hijas a definir cómo se calcula su precio.
        (Ej: Un producto comercial retorna el precio_base, pero uno preparado podría sumar los ingredientes).
        """
        pass