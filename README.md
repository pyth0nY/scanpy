# 🛡️ CyberScan v1.5

![CyberScan v1.5]

Un escáner de puertos y servicios construido con **Python** y **PySide6**. Este proyecto combina una interfaz gráfica moderna con funcionalidades de red para crear una herramienta educativa y funcional, ideal para aprender sobre programación de redes, multithreading y desarrollo de GUIs.

---

## ✨ Características Principales

-   **Interfaz Gráfica Intuitiva:** Tema oscuro profesional diseñado con QSS para una experiencia de usuario agradable.
-   **Escaneo Flexible:**
    -   Selección rápida de los **puertos más comunes**.
    -   Opción para escanear un **rango de puertos personalizado** (ej. 1-1024).
-   **Banner Grabbing:** No solo detecta si un puerto está abierto, sino que intenta capturar el "banner" para identificar el software y la versión del servicio.
-   **Multithreading (`QThread`):** El proceso de escaneo se ejecuta en un hilo secundario, garantizando que la interfaz permanezca **100% responsiva** en todo momento.
-   **Detección de IP Pública:** Un botón para obtener tu IP pública al instante usando una API externa.
-   **Exportación de Resultados:** Guarda los resultados del escaneo en formato `.txt` o `.csv` para un análisis posterior.
-   **Menú Completo:** Barra de menú con opciones de exportación y una ventana "Acerca de".

---

## 🛠️ Tecnologías Utilizadas

-   **Lenguaje:** `Python 3`
-   **Interfaz Gráfica:** `PySide6 (Qt for Python)`
-   **Estilos:** `QSS (Qt Style Sheets)`
-   **Red:** Módulo `socket` nativo de Python.
-   **Peticiones HTTP:** Librería `requests`.

---

## 🚀 Instalación y Puesta en Marcha

Para ejecutar CyberScan en tu máquina local, sigue estos pasos.

### 1. Prerrequisitos

-   **Python 3.8+** instalado.
-   Se recomienda el uso de un **entorno virtual** para mantener las dependencias aisladas.

### 2. Configuración del Proyecto

**1. Clona el repositorio:**

git clone (https://github.com/pyth0nY/scanpy)
cd cyberscan

### 📁 Estructura del Proyecto

-   **`icons/`**: Cont como __pycache__ y .venv
├── cyberscan.py          # Código fuente principal de la aplicación
├──iene todos los iconos vectoriales (`.svg`) utilizados en la interfaz.
-   **`cyberscan. README.md             # Este archivo
├── requirements.txt      # Lista de dependencias de Python
├── resources.qrc         py`**: El corazón de la aplicación, contiene toda la lógica y la definición de la GUI.
-   **`requirements.# Archivo XML que lista los recursos (iconos)
├── resources_rc.py       # Archivo autogenerado por pyside6-rcc (NO TOCAR)
└── style.qss             # Hojaás que la diferencia es como de la noche al díatxt`**: Lista las dependencias de Python para una fácil instalación (`pip install -r requirements.txt`).
-    de estilos para la interfaz gráfica
### ⚠️ Advertencia de Uso Ético
Este software se ha desarrollado con fines puramente educativos y para la autoevaluación de seguridad.
### 🔴 NO UTILICES ESTA HERRAMIENTA EN REDES O SISTEMAS QUE NO SEAN DE TU PROPIEDAD o sobre los que no tengas permiso explícito y por escrito.
El escaneo de puertos no autorizado es ilegal en muchas jurisdicciones y se considera una actividad hostil.
El uso indebido de esta herramienta es responsabilidad exclusiva del usuario. Actúa con ética y responsabilidad.
