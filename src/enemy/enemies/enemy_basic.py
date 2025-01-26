import pygame
import os
from src.game_object.live_character import LiveCharacter
from typing import List


class EnemyBasic(LiveCharacter):
    health: int = 100
    max_health: int = 100
    damage: int = 10
    position: tuple[int, int] = (0, 0)
    current_frame: int = 0
    sprites: List[pygame.Surface] = []
    frame_rate: int = 100
    last_update: int = 0

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.position = position
        # Tiempo de la última actualización
        self.last_update = pygame.time.get_ticks()

        # Obtener la ruta absoluta del directorio actual (enemy_basic.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir la ruta correcta hacia el sprite (retrocedemos dos niveles)
        sprite_path = os.path.join(
            current_dir,
            "../../../assets/enemies/basic/1.png",
        )

        # Normalizar la ruta para asegurarse de que sea válida
        sprite_path = os.path.normpath(sprite_path)

        # Llamar al método estático load_sprite
        self.sprites = self.load_sprite(
            sprite_path,
            (488, 220),
            (2, 4),
            iterate_all=True,
            flipped=True,
            scale_factor=1.3,
        )
