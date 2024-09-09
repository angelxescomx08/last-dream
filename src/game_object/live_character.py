from abc import abstractmethod
from src.game_object.animated_object import AnimatedObject

class LiveCharacter(AnimatedObject):

  @property
  @abstractmethod
  def health(self) -> int:
    pass

  @property
  @abstractmethod
  def damage(self) -> int:
    pass