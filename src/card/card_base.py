from abc import ABC, abstractmethod
from typing import Callable
from pygame import Rect, Surface

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
  def hover(self) -> None:
    pass

  @abstractmethod
  def drag(self) -> None:
    pass

  @abstractmethod
  def draw(self) -> None:
    pass
