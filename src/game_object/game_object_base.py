from abc import ABC, abstractmethod

import pygame

class GameObjectBase(ABC):
  
  @property
  @abstractmethod
  def position(self) -> tuple[int, int]:
    pass
  
  @property
  @abstractmethod
  def flipped(self) -> bool:
    pass
  
  @property
  @abstractmethod
  def scale_factor(self) -> float:
    pass

  @property
  @abstractmethod
  def rect(self) -> pygame.Rect:
    pass