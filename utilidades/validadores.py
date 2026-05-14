import re
def validar_solo_numeros(valor: str, nombre_campo: str) -> str:
    valor_limpio = validar_cadena_no_vacia(valor, nombre_campo)
    if not valor_limpio.isdigit():
        raise ValueError(f"El campo '{nombre_campo}' solo debe contener números. Recibido: '{valor_limpio}'")
    return valor_limpio

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

    # 1. Convertimos la entrada y las opciones a minúsculas para una comparación segura
    valor_comparacion = valor_limpio.lower()
    opciones_comparacion = [opcion.lower() for opcion in opciones_validas]

    # 2. Comparamos
    if valor_comparacion not in opciones_comparacion:
        raise ValueError(f"El campo '{nombre_campo}' debe ser uno de {opciones_validas}. Recibido: '{valor_limpio}'")

    # 3. Retornamos el valor formateado (Primera letra en mayúscula por estética)
    return valor_comparacion.capitalize()

def validar_numero_positivo(valor: float, nombre_campo: str, permite_cero: bool = True) -> float:
    """Valida que un valor sea numérico y no sea negativo."""
    try:
        numero = float(valor)
    except ValueError:
        raise ValueError(f"El campo '{nombre_campo}' debe ser un número válido.")
    if numero < 0:
        raise ValueError(f"El campo '{nombre_campo}' no puede ser negativo.")
    if not permite_cero and numero == 0:
        raise ValueError(f"El campo '{nombre_campo}' debe ser mayor a cero.")
    return numero

def validar_correo(valor: str) -> str:
    # Excepción explícita para cuando no se requiere factura electrónica
    if valor == "No aplica":
        return valor

    valor_limpio = validar_cadena_no_vacia(valor, "correo electrónico")
    # Regex básico para validar formato de correo electrónico
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", valor_limpio):
        raise ValueError(f"Formato de correo inválido. Recibido: '{valor_limpio}'")
    return valor_limpio