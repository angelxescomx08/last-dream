import pygame
from src.card.card_base import CardBase

class AttackCard(CardBase):
  screen: pygame.Surface
  rect: pygame.Rect = pygame.Rect(0, 0, 100, 150)
  is_hovered: bool = False
  is_dragged: bool = False
  initial_position: tuple[int,int] = (0, 0)
  position: tuple[int,int] = (0, 0)
  name: str = "Attack"
  cost: int = 1
  description: str = "Deal 5 damage"

  def __init__(self, screen: pygame.Surface, position: tuple[int,int] = (0, 0)):
    super().__init__()
    self.screen = screen
    self.rect = pygame.Rect(0, 0, 100, 150)
    self.is_hovered = False
    self.is_dragged = False
    self.position = position
    self.initial_position = position
    self.name = "Attack"
    self.cost = 1
    self.description = "Deal 5 damage"

  def effect(self):
    pass
