import re

def validar_cadena_no_vacia(valor: str, nombre_campo: str) -> str:
    if not valor or not str(valor).strip():
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
    return str(valor).strip()

def validar_solo_letras(valor: str, nombre_campo: str) -> str:
    valor_limpio = validar_cadena_no_vacia(valor, nombre_campo)
    # Expresión regular para permitir letras y espacios (nombres compuestos)
    if not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", valor_limpio):
        raise ValueError(f"El campo '{nombre_campo}' solo debe contener letras. Recibido: '{valor_limpio}'")
    return valor_limpio

def validar_telefono(valor: str) -> str:
    valor_limpio = validar_cadena_no_vacia(valor, "teléfono")
    if not valor_limpio.isdigit() or len(valor_limpio) < 7:
        raise ValueError(f"El teléfono debe tener mínimo 7 dígitos y contener solo números. Recibido: '{valor_limpio}'")
    return valor_limpio

def validar_opciones(valor: str, opciones_validas: list, nombre_campo: str) -> str:
    valor_limpio = validar_cadena_no_vacia(valor, nombre_campo)
    if valor_limpio not in opciones_validas:
        raise ValueError(f"El campo '{nombre_campo}' debe ser uno de {opciones_validas}. Recibido: '{valor_limpio}'")
    return valor_limpio