# Sistema de Gestión de Restaurante (Fast-Food POS) - Proyecto Final

Este repositorio contiene la solución al proyecto final de la asignatura **Programación I**, el cual modela un sistema de información transaccional para un restaurante de comidas rápidas, aplicando rigurosamente los pilares de la Programación Orientada a Objetos (POO) y principios de diseño SOLID en Python.

## 📋 Información Académica
* **Institución:** Universidad de Manizales
* **Facultad:** Ingeniería
* **Asignatura:** Programación I (Segundo Semestre)
* **Estudiantes:**
  * Johan Marcelo Rojas
* **Formato de entrega:** Repositorio estructurado y archivos `.py` documentados.

---

## 🎯 Criterios de Evaluación y Aplicación en el Código

El sistema cumple a cabalidad con las directrices académicas mediante las siguientes implementaciones:

### 1. Uso del Método Constructor (`__init__`)
Todas las entidades del sistema validan su estado inicial desde el momento de su instanciación. Se inyectan validadores puros para asegurar que, por ejemplo, un `Ingrediente` no nazca con un costo negativo, o que un `Cajero` no inicie con un turno inexistente.

### 2. Creación de Métodos y Abstracción
Se abstrajo la lógica de negocio aislando responsabilidades (Principio SRP):
*   **Inventario:** Métodos como `agregar_ingrediente()` y `consumir_stock()` gestionan el inventario.
*   **Pedidos:** Métodos como `agregar_producto()` y `procesar_pedido()` unen actores y catálogo.
*   **Contratos Base:** Uso de clases abstractas (`Persona`, `Producto`) para obligar a las clases hijas a implementar métodos como `mostrar_informacion()` y `calcular_precio_final()`.

### 3. Instancia de Objetos (Composición y Relaciones)
El archivo `main.py` orquesta la instanciación simulando el flujo real:
*   La materia prima (`Ingrediente`) compone la *receta* de un `ProductoPreparado`.
*   El `Pedido` recibe las instancias de `Cliente` y `Cajero` al abrirse.

---

## 🚀 Características y Lógica de Negocio Destacadas

*   **Tolerancia a Fallos (UX):** El sistema utiliza bucles de reintento (`while True`) y bloques `try-except` para atrapar errores de digitación del usuario sin colapsar la aplicación.
*   **Gestor de Inventario en Tiempo Real:** Al procesar un pedido de un producto preparado (ej. Hamburguesa), el sistema lee su diccionario de receta interna y descuenta automáticamente los ingredientes de la bodega central.
*   **Lógica de Facturación (Consumidor Final vs Electrónica):** Implementación de reglas de negocio reales. Permite el ingreso rápido (ID genérico "2222222222") para agilizar la fila, o solicita los datos completos si el cliente exige Factura Electrónica.