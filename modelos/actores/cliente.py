from core.abstract_persona import Persona
from utilidades.validadores import validar_telefono

class Cliente(Persona):
    """
    Entidad que representa a un cliente del restaurante.
    Hereda de la clase abstracta Persona.
    """
    def __init__(self, identificacion: str, nombre: str, telefono: str):
        # 1. Llamamos al constructor del padre para inicializar identificación y nombre
        super().__init__(identificacion, nombre)
        # 2. Inicializamos el atributo específico del hijo
        self._telefono = validar_telefono(telefono)

    @property
    def telefono(self) -> str:
        return self._telefono

    # 3. Cumplimos el contrato: Implementamos el método abstracto obligatorio
    def mostrar_informacion(self) -> str:
        return f"[CLIENTE] Nombre: {self.nombre} | ID: {self.identificacion} | Tel: {self.telefono}"