from abc import ABC, abstractmethod

class MetodoPago(ABC):
    """
    Interfaz para los procesadores de pago.
    Cumple con el principio de Inversión de Dependencias (DIP).
    """
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        """
        Todo método de pago (Efectivo, Tarjeta, etc.) debe implementar esta rutina.
        """
        pass