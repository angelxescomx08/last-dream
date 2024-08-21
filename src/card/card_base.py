from abc import ABC, abstractmethod
from typing import Callable

class CardBase(ABC):

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
  def activate_effect(self) -> None:
    pass
