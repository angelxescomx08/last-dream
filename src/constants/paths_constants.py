import os

# Obtener la ruta absoluta del directorio actual
current_path = os.path.abspath(os.path.dirname(__file__))

# Retroceder un directorio para llegar a la raíz del proyecto
root_path = os.path.abspath(os.path.join(current_path, "..", ".."))

PATH_CARD_BACKGROUNDS = os.path.join(
  root_path, "assets", "card", "backgrounds.png"
)