# scanpy
¡Por supuesto, bro! Un buen proyecto merece un README.md a la altura. Un README es la carta de presentación, lo primero que la gente ve. Tiene que ser claro, directo y con estilo.

Aquí tienes un README completo y profesional para tu proyecto, basado en la estructura de archivos y el código final que hemos construido.

Instrucciones:

En la carpeta de tu proyecto, crea un nuevo archivo llamado README.md.

Copia y pega todo el texto que está a continuación dentro de ese archivo.

¡Importante! Haz una captura de pantalla de tu aplicación funcionando y guárdala en la carpeta del proyecto con el nombre screenshot.png para que se vea en el README.

(Copia y pega todo lo que está debajo de esta línea en tu archivo README.md)
🛡️ CyberScan v1.0

Un escáner de puertos simple pero funcional, construido con Python y PySide6. Creado con fines educativos para aprender sobre redes y ciberseguridad, y para ayudar a usuarios a identificar puertos abiertos en sus propias redes.

![alt text](screenshot.png)

(Reemplaza este texto con una captura de pantalla de tu aplicación y nombra el archivo screenshot.png)

🚀 Sobre el Proyecto

Este proyecto nació de la idea de crear una herramienta visual e intuitiva que permitiera a cualquier persona, sin necesidad de ser un experto en ciberseguridad, analizar su propia red. Utiliza sockets de Python para comprobar el estado de los puertos y una interfaz gráfica moderna construida con PySide6 para una experiencia de usuario agradable.

Tecnologías utilizadas:

Python 3: Como lenguaje principal.

PySide6 (Qt for Python): Para la creación de la interfaz gráfica.

Sockets: Para la lógica de red y el escaneo de puertos.

QSS (Qt Style Sheets): Para personalizar el aspecto y darle el tema oscuro.

✨ Funcionalidades

✅ Escaneo de Puertos Comunes: Una lista predefinida con los puertos más utilizados para un análisis rápido.

✅ Escaneo por Rango: Permite al usuario definir un rango de puertos personalizado (ej: 1-1024).

✅ Detección de IP Pública: Un botón para obtener y escanear automáticamente tu IP pública.

✅ Interfaz Gráfica Moderna: Un tema oscuro y un diseño limpio para que sea fácil de usar.

✅ Escaneo No Bloqueante: Gracias al uso de hilos (QThread), la interfaz nunca se congela durante un escaneo.

✅ Diseño Modular: El código está organizado en clases para facilitar su lectura y mantenimiento.

⚙️ Instalación y Uso

¡Vamos al lío! Para poner en marcha CyberScan, sigue estos pasos:

1. Prerrequisitos

Asegúrate de tener Python 3 instalado en tu sistema. Si no lo tienes, puedes descargarlo desde python.org. Durante la instalación en Windows, ¡no olvides marcar la casilla "Add Python to PATH"!

2. Clonar o Descargar el Repositorio

Obtén una copia de los archivos del proyecto en tu máquina local.

Generated bash
# Si usas Git (recomendado)
git clone https://ruta-a-tu-repositorio.git
cd nombre-del-proyecto

3. Instalar Dependencias

Este proyecto necesita algunas librerías de Python. Instálalas con pip:

Generated bash
pip install pyside6 requests
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
4. Compilar los Recursos (¡Paso Crucial!)

La interfaz utiliza iconos personalizados (.svg). Para que la aplicación los encuentre, necesitamos empaquetarlos en un archivo de Python.

Ejecuta el siguiente comando en la terminal, estando en la carpeta del proyecto:

Generated bash
# Este comando lee el `resources.qrc` y crea `resources_rc.py`
pyside6-rcc resources.qrc -o resources_rc.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Consejo Pro: Para evitar problemas de entorno, es más seguro usar:

Generated bash
python -m PySide6.rcc resources.qrc -o resources_rc.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
5. ¡Ejecutar la Aplicación!

¡Ya está todo listo! Lanza la aplicación con:

Generated bash
python cyberscan.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

¡Y listo! Ya deberías ver la ventana de CyberScan lista para escanear.

📁 Estructura de Archivos
Generated code
CYBERSCAN V1.0/
├── icons/              # Carpeta con todos los iconos SVG
│   ├── ip.svg
│   ├── scan.svg
│   └── ...
├── cyberscan.py         # El código principal de la aplicación
├── resources.qrc         # La lista de recursos para Qt (iconos)
├── resources_rc.py     # Archivo autogenerado con los recursos compilados (NO EDITAR)
├── style.qss           # La hoja de estilos que le da el look & feel a la app
└── README.md           # Este archivo
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END
⚠️ Advertencia Ética

Este software ha sido creado con fines estrictamente educativos y de autoevaluación.

USA ESTA HERRAMIENTA ÚNICAMENTE EN REDES Y SISTEMAS DE TU PROPIEDAD o en aquellos donde tengas permiso explícito y por escrito para realizar un análisis.

Escanear puertos de una red ajena sin autorización es ilegal en la mayoría de jurisdicciones y se considera una actividad maliciosa.

El autor no se hace responsable del mal uso de esta herramienta. ¡Sé responsable y ético!
