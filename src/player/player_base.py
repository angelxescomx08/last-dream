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
    if not pygame.mouse.get_pressed()[0]:
      return
    mouse_pos = pygame.mouse.get_pos()
    for enemy in self.enemies:
      if enemy.rect.collidepoint(mouse_pos):
        self.targeted_enemy = enemy
      else:
        self.targeted_enemy = None