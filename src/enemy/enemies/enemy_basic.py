import pygame
import os
from src.enemy.enemy_base import EnemyBase
from typing import List, Tuple

class EnemyBasic(EnemyBase):
  health: int = 100
  damage: int = 10
  position: tuple[int, int] = (0, 0)
  current_frame: int = 0
  sprites: List[pygame.Surface] = []

  def __init__(self, position: tuple[int, int]):
    super().__init__()
    self.position = position
    self.last_update = pygame.time.get_ticks()  # Tiempo de la última actualización
    self.frame_rate = 100  # Intervalo de tiempo en milisegundos entre cuadros (ajustar según sea necesario)

    # Obtener la ruta absoluta del directorio actual (enemy_basic.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta correcta hacia el sprite (retrocedemos dos niveles)
    sprite_path = os.path.join(current_dir, "../../../assets/enemies/basic/1.png")

    # Normalizar la ruta para asegurarse de que sea válida
    sprite_path = os.path.normpath(sprite_path)

    # Llamar al método estático load_sprite
    self.sprites = EnemyBase.load_sprite(
      sprite_path, (488, 220), (2, 4), iterate_all=True
    )

  def update(self, screen: pygame.Surface):
    current_time = pygame.time.get_ticks()  # Obtener el tiempo actual
    
    if current_time - self.last_update > self.frame_rate:
      self.last_update = current_time  # Actualizar el tiempo de la última actualización
      self.current_frame = (self.current_frame + 1) % len(self.sprites)  # Cambiar al siguiente cuadro
    
    screen.blit(self.sprites[self.current_frame], self.position)
