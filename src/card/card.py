from typing import Callable
import pygame
import os

class Card:
  image: str
  mana: int
  effect: Callable
  def __init__(self, image: str, mana: int, effect: Callable, current_directory: str):
    self.image = image
    self.mana = mana
    self.effect = effect
    self.load_sprite(current_directory)
  
  def load_sprite(self, current_directory: str) -> None:
    sprite_sheet_path = os.path.join(
      current_directory,
      'assets/card/assets_cards.png'
    )

  def draw(self):
    pass
