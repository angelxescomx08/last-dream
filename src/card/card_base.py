from abc import ABC, abstractmethod
from pygame import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND, Rect, Surface, mouse, draw

class CardBase(ABC):
  @property
  @abstractmethod
  def rect(self) -> Rect:
    pass

  @property
  @abstractmethod
  def is_hovered(self) -> bool:
    pass

  @is_hovered.setter
  @abstractmethod
  def is_hovered(self, value: bool):
    pass

  @property
  @abstractmethod
  def is_dragged(self) -> bool:
    pass

  @is_dragged.setter
  @abstractmethod
  def is_dragged(self, value: bool):
    pass

  @property
  @abstractmethod
  def position(self) -> tuple[int, int]:
    pass

  @position.setter
  @abstractmethod
  def position(self, value: tuple[int, int]):
    pass

  @abstractmethod
  def play(self) -> None:
    pass

  def set_position(self, position: tuple[int, int]) -> None:
    self.position = position

  def drag(self) -> None:
    if mouse.get_pressed()[0] and self.rect.collidepoint(mouse.get_pos()):
      self.is_dragged = True

    if self.is_dragged:
      center_pos = (
        mouse.get_pos()[0] - self.rect.width // 2,
        mouse.get_pos()[1] - self.rect.height // 2
      )
      mouse.set_cursor(SYSTEM_CURSOR_HAND)
      self.position = center_pos

    if self.is_dragged and not mouse.get_pressed()[0]:
      self.is_dragged = False

  def hover(self):
    mouse_pos = mouse.get_pos()
    if self.rect.collidepoint(mouse_pos):
      self.is_hovered = True
      mouse.set_cursor(SYSTEM_CURSOR_HAND)
    else:
      self.is_hovered = False
      mouse.set_cursor(SYSTEM_CURSOR_ARROW)

  def draw(self, screen: Surface):
    self.hover()
    self.drag()

    color = (255, 255, 255) if not self.is_hovered else (200, 200, 200)
    self.rect.topleft = self.position
    draw.rect(screen, color, self.rect)
