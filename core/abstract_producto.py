from abc import ABC, abstractmethod

class Producto(ABC):
    """
    Clase abstracta para los elementos del catálogo.
    """
    def __init__(self, nombre: str, precio_base: float):
        # 'precio_base' es un candidato ideal para un validador de números positivos
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """
        Método abstracto: Obliga a las clases hijas a definir cómo se calcula su precio.
        (Ej: Un producto comercial retorna el precio_base, pero uno preparado podría sumar los ingredientes).
        """
        pass