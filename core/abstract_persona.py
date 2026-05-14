from abc import ABC, abstractmethod
from utilidades.validadores import validar_cadena_no_vacia, validar_solo_letras

class Persona(ABC):
    """
    Clase abstracta que define la estructura base para cualquier persona en el sistema.
    No se puede instanciar directamente.
    """
    def __init__(self, identificacion: str, nombre: str):
        # Aquí ya podemos notar que 'identificacion' y 'nombre' necesitarán validadores genéricos
        self._identificacion = validar_cadena_no_vacia(identificacion, "identificación")
        self._nombre = validar_solo_letras(nombre, "nombre")

    @property
    # El uso de @property es un buen ejemplo de encapsulamiento, permitiendo controlar el acceso a los atributos.
    def nombre(self) -> str:
        return self._nombre

    @property
    # El método 'identificacion' también es un candidato para un validador de formato específico (ej: DNI, RUC, etc.).
    def identificacion(self) -> str:
        return self._identificacion

    @abstractmethod
    # El método 'mostrar_informacion' es un buen ejemplo de cómo forzar a las clases hijas a implementar su propia lógica de presentación.
    def mostrar_informacion(self) -> str:
        """
        Método abstracto: Toda clase hija DEBE implementar cómo muestra su información.
        """
        pass