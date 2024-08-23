import pygame
from src.card.card_base import CardBase

class AttackCard(CardBase):
  rect: pygame.Rect = pygame.Rect(0, 0, 100, 150)
  is_hovered: bool = False
  is_dragged: bool = False
  position: tuple[int,int] = (0, 0)
  name: str = "Attack"
  cost: int = 1
  description: str = "Deal 5 damage"

  def __init__(self, screen: pygame.Surface):
    super().__init__()
    self.screen = screen

  def effect(self):
    pass

  def play(self):
    pass

  def hover(self):
    if self.is_hovered:
      self.position = pygame.mouse.get_pos()

  def drag(self):
    pass

  def draw(self):
    pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
