from abc import ABC, abstractmethod
from typing import List
from pygame import Surface

from src.card.card_base import CardBase

class HandBase(ABC):

  @property
  @abstractmethod
  def cards(self) -> List[CardBase]:
    pass

  def draw(self, screen: Surface) -> None:
    for card in self.cards:
      card.draw(screen)