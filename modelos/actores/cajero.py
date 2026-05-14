from core.abstract_persona import Persona
from utilidades.validadores import validar_cadena_no_vacia, validar_opciones

class Cajero(Persona):
    """
    Entidad que representa al empleado encargado de procesar los pedidos.
    Hereda de la clase abstracta Persona.
    """
    def __init__(self, identificacion: str, nombre: str, codigo_empleado: str, turno: str):
        # 1. Llamamos al constructor del padre
        super().__init__(identificacion, nombre)
        # 2. Inicializamos atributos específicos
        self._codigo_empleado = validar_cadena_no_vacia(codigo_empleado, "código de empleado")
        self._turno = validar_opciones(turno, ["mañana", "tarde", "noche"], "turno")

    @property
    def codigo_empleado(self) -> str:
        return self._codigo_empleado

    @property
    def turno(self) -> str:
        return self._turno

    # 3. Cumplimos el contrato: Implementamos el método abstracto obligatorio
    def mostrar_informacion(self) -> str:
        return f"[CAJERO] Nombre: {self.nombre} | Código: {self.codigo_empleado} | Turno: {self.turno}"