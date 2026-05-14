from core.abstract_persona import Persona
from utilidades.validadores import validar_telefono, validar_solo_numeros, validar_correo

class Cliente(Persona):
    """
    Entidad que representa a un cliente del restaurante.
    Hereda de la clase abstracta Persona.
    """
    def __init__(self, identificacion: str, nombre: str, telefono: str, correo: str = "No aplica"):
        # Validamos que la identificación sea estrictamente numérica antes de enviarla al Padre
        id_valida = validar_solo_numeros(identificacion, "identificación (Cédula/NIT)")

        super().__init__(id_valida, nombre)
        self._telefono = validar_telefono(telefono)
        self._correo = validar_correo(correo)

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def correo(self) -> str:
        return self._correo

    def mostrar_informacion(self) -> str:
        return f"[CLIENTE] {self.nombre} | ID: {self.identificacion} | Tel: {self.telefono} | Email: {self.correo}"