from abc import ABC, abstractmethod
from typing import Callable
from pygame import Rect, Surface, mouse, draw

class CardBase(ABC):

  @property
  @abstractmethod
  def rect(self) -> Rect:
    pass

  @property
  @abstractmethod
  def is_hovered(self) -> bool:
    pass

  @property
  @abstractmethod
  def is_dragged(self) -> bool:
    pass

  @property
  @abstractmethod
  def position(self) -> tuple[int, int]:
    pass

  @property
  @abstractmethod
  def name(self) -> str:
    pass

  @property
  @abstractmethod
  def cost(self) -> int:
    pass

  @property
  @abstractmethod
  def description(self) -> str:
    pass

  @property
  @abstractmethod
  def effect(self) -> Callable:
    pass

  @abstractmethod
  def play(self) -> None:
    pass

  @abstractmethod
  def draw(self) -> None:
    pass
  
  def drag(self) -> None:
    if self.is_dragged:
      center_pos = (
        mouse.get_pos()[0] - self.rect.width // 2, 
        mouse.get_pos()[1] - self.rect.height // 2
      )
      self.position = center_pos
      
    if self.is_dragged and not mouse.get_pressed()[0]:
      self.is_dragged = False
      
    if mouse.get_pressed()[0] and self.rect.collidepoint(mouse.get_pos()):
      self.is_dragged = True

  def hover(self):
    mouse_pos = mouse.get_pos()
    if self.rect.collidepoint(mouse_pos):
      self.is_hovered = True
    else:
      self.is_hovered = False
      
  def draw(self, screen: Surface):
    self.hover()
    self.drag()
    color = (255, 255, 255) if not self.is_hovered else (200, 200, 200)

    #sustitute position with self.position
    self.rect.topleft = self.position
    
    draw.rect(screen, color, self.rect)