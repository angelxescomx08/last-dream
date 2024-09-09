from abc import abstractmethod
from typing import List, Tuple

import pygame
from src.game_object.game_object_base import GameObjectBase

class AnimatedObject(GameObjectBase):

  position: tuple[int, int] = (0, 0)
  flipped: bool = False
  scale_factor: float = 1.0

  @property
  @abstractmethod
  def current_frame(self) -> int:
    pass

  @property
  @abstractmethod
  def frame_rate(self) -> int:
    pass

  @property
  @abstractmethod
  def last_update(self) -> int:
    pass

  @property
  @abstractmethod
  def sprites(self) -> List[pygame.Surface]:
    pass

  def scale(
    self, 
    sprites: List[pygame.Surface], 
    scale_factor: float
  ) -> List[pygame.Surface]:
    # Escalar todos los cuadros del sprite
    return [pygame.transform.scale(sprite, (
      int(sprite.get_width() * scale_factor), 
      int(sprite.get_height() * scale_factor)
    )) for sprite in sprites]

  @staticmethod
  def load_sprite(
    image_path: str, 
    sprite_size: Tuple[int, int], 
    grid_size: Tuple[int, int],
    row_to_animate: int = 0,
    iterate_all: bool = True, 
    flipped: bool = False, 
    scale_factor: float = 1.0
  ) -> List[pygame.Surface]:
    # Cargar la imagen
    sprite_sheet = pygame.image.load(image_path).convert_alpha()
    sheet_width, sheet_height = sprite_sheet.get_size()

    # Extraer el tamaño total y la cantidad de filas y columnas
    total_width, total_height = sprite_size
    rows, cols = grid_size

    # Calcular el tamaño de cada cuadro
    frame_width = total_width // cols
    frame_height = total_height // rows

    # Asegúrate de que los tamaños calculados no sean mayores que la imagen
    if frame_width > sheet_width or frame_height > sheet_height:
      raise ValueError("El tamaño del cuadro excede el tamaño de la imagen.")

    # Lista para almacenar los cuadros individuales del sprite
    sprites = []

    # Si iterate_all es True, iteramos por todas las filas, de lo contrario solo por row_to_animate
    rows_to_iterate = range(rows) if iterate_all else [row_to_animate]

    for row in rows_to_iterate:
      for col in range(cols):
        # Calcular la posición del cuadro
        x = col * frame_width
        y = row * frame_height

        # Verificar que el recorte esté dentro de los límites de la imagen
        if x + frame_width <= sheet_width and y + frame_height <= sheet_height:
          # Recortar el cuadro de la imagen original
          frame = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
          # Invertir el cuadro si se requiere
          if flipped:
            frame = pygame.transform.flip(frame, True, False)
          sprites.append(frame)
        else:
          raise ValueError("El recorte está fuera de los límites de la imagen.")
      
    # Asegúrate de que el factor de escala sea válido
    if scale_factor <= 0:
      raise ValueError("El factor de escala debe ser mayor que 0.")
    
    # Escalar los sprites si es necesario
    sprites = [pygame.transform.scale(sprite, (
      int(sprite.get_width() * scale_factor), 
      int(sprite.get_height() * scale_factor),
    )) for sprite in sprites]

    return sprites


  def update(self, screen: pygame.Surface):
    # Obtener el tiempo actual
    current_time = pygame.time.get_ticks()

    if current_time - self.last_update > self.frame_rate:
      # Actualizar el tiempo de la última actualización
      self.last_update = current_time
      # Cambiar al siguiente cuadro
      self.current_frame = (self.current_frame + 1) % len(self.sprites)

    # Dibuja el sprite actual en la pantalla
    screen.blit(self.sprites[self.current_frame], self.position)