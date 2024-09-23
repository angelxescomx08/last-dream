from abc import abstractmethod
from typing import List

import pygame
from src.game_object.live_character import LiveCharacter

class PlayerBase(LiveCharacter):
  @property
  @abstractmethod
  def enemies(self) -> List[LiveCharacter]:
    pass

  @property
  @abstractmethod
  def targeted_enemy(self) -> LiveCharacter:
    pass

  def target_enemy(self):
    mouse_pos = pygame.mouse.get_pos()
    for enemy in self.enemies:
      if enemy.rect.collidepoint(mouse_pos):
        self.targeted_enemy = enemy
        # print(f"Targeted enemy: {self.targeted_enemy}")
      else:
        self.targeted_enemy = None