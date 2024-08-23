# Mi Videojuego con Pygame y Pydantic
Este es un proyecto de videojuego desarrollado en Python utilizando las bibliotecas Pygame y Pydantic.

# Pasos para ejecutar el proyecto
Python 3.8 o superior
Instalación
Sigue los pasos a continuación para configurar y ejecutar el proyecto en tu máquina local.

1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/mi_videojuego.git
cd mi_videojuego
```

2. Crea un entorno virtual
Es recomendable trabajar en un entorno virtual para mantener las dependencias aisladas.

```bash
python -m venv venv
```

3. Activa el entorno virtual
En Windows:

```bash
venv\Scripts\activate
```
En macOS/Linux:

```bash
source venv/bin/activate
```

4. Instala las dependencias
Con el entorno virtual activado, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

5. Ejecuta el juego
Una vez instaladas las dependencias, puedes ejecutar el juego con el siguiente comando:

```bash
python main.py
```

Se puede usar nodemon para reiniciar la app automáticamente cada vez que se guarden cambios en los archivos.

```bash
nodemon main.py
```

# Estructura del proyecto

```
last-dream/
│
├── venv/               # Entorno virtual
├── main.py             # Archivo principal del juego
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación del proyecto
└── .gitignore          # Archivos y carpetas ignorados por git
```