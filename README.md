# Sistema de Gestión de Restaurante - Proyecto Final

Este repositorio contiene la solución al proyecto final de la asignatura **Programación I**, el cual modela un sistema de información de la vida diaria (la operación de un restaurante) aplicando los pilares de la Programación Orientada a Objetos (POO) en Python.

## 📋 Información Académica
* **Institución:** Universidad de Manizales
* **Programa:** Ingeniería de Sistemas
* **Estudiante:** Johan Marcelo Rojas
* **Asignatura:** Programación I

Programacion-1_Proyecto_Final_Restaurante/
│
├── README.md                  # 🎯 CORREGIDO: Siempre en la raíz
├── .gitignore                 # En la raíz: Define qué archivos ignorar (ej. __pycache__)
├── requirements.txt           # En la raíz: Lista de librerías externas (si usas alguna)
├── main.py                    # ⚙️ En la raíz: Punto de entrada (Fácil de encontrar y ejecutar)
│
└── src/                       # 📦 Carpeta principal del código fuente
    ├── __init__.py
    │
    ├── core/                  # 🔵 Abstracciones (Reglas base - Principio DIP)
    │   ├── __init__.py
    │   ├── abstract_persona.py
    │   ├── abstract_producto.py
    │   └── interface_pago.py
    │
    ├── models/                # 🟢 Entidades Concretas (Principio SRP)
    │   ├── __init__.py
    │   ├── actores/           # cliente.py, cajero.py
    │   └── catalogo/          # prod_comercial.py, prod_preparado.py
    │
    ├── services/              # 🟠 Lógica de Negocio y Operaciones (Principio OCP)
    │   ├── __init__.py
    │   ├── pedido.py          # Transacción principal
    │   ├── procesador_pagos.py
    │   └── restaurante.py     # Controlador general
    │
    └── utils/                 # 🛠️ NUEVO: Utilidades transversales (Principio DRY)
        ├── __init__.py
        └── validadores.py     # Ej: validar_cadena(), validar_numero_positivo()