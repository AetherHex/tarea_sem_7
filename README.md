# Sistema de Gestión de Restaurante (restaurante_app)

Este proyecto es una aplicación de consola modular desarrollada en Python bajo los principios de la Programación Orientada a Objetos (POO). El diseño arquitectónico ha sido estructurado por capas para separar los modelos de datos de la lógica de servicio, cumpliendo estrictamente con las directrices académicas de la evaluación de la Semana 7.

* **Estudiante:** Aarón
* **Asignatura:** Programación Orientada a Objetos
* **Contexto:** Maestría en Educación Básica / Gestión Educativa

---

## 1. Estructura del Proyecto

El sistema se organiza de forma modular para garantizar la escalabilidad, el mantenimiento y la separación de responsabilidades:

```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py
