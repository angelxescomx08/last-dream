import pygame
import os
from typing import List, Tuple
from abc import ABC, abstractmethod

class EnemyBase(ABC):

  @property
  @abstractmethod
  def health(self) -> int:
    pass

  @property
  @abstractmethod
  def damage(self) -> int:
    pass

  @property
  @abstractmethod
  def position(self) -> tuple[int, int]:
    pass

  @property
  @abstractmethod
  def current_frame(self) -> int:
    pass

  @property
  @abstractmethod
  def sprites(self) -> List[pygame.Surface]:
    pass

  @staticmethod
  def load_sprite(image_path: str, sprite_size: Tuple[int, int], grid_size: Tuple[int, int], iterate_all: bool = True) -> List[pygame.Surface]:
    # Cargar la imagen
    sprite_sheet = pygame.image.load(image_path).convert_alpha()
    sheet_width, sheet_height = sprite_sheet.get_size()

    # Extraer el tamaño total y la cantidad de filas y columnas
    total_width, total_height = sprite_size
    rows, cols = grid_size

    # Calcular el tamaño de cada cuadro
    frame_width = total_width // cols
    frame_height = total_height // rows

    # Lista para almacenar los cuadros individuales del sprite
    sprites = []

    for row in range(rows):
      for col in range(cols):
        if not iterate_all and row > 0:
          break  # Si no se debe iterar por todas las filas, salimos del bucle
        
        # Calcular la posición del cuadro
        x = col * frame_width
        y = row * frame_height
        
        # Verificar que el recorte esté dentro de los límites de la imagen
        if x + frame_width <= sheet_width and y + frame_height <= sheet_height:
          # Recortar el cuadro de la imagen original
          frame = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
          sprites.append(frame)
        else:
          raise ValueError("El recorte está fuera de los límites de la imagen.")
    
    return sprites
