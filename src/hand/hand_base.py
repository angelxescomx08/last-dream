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
    # Dibuja todas las cartas excepto la que se está arrastrando
    for card in self.cards:
      if card is not CardBase._dragging_card:
        card.draw(screen)

    # Dibuja la carta que se está arrastrando encima de todas
    if CardBase._dragging_card:
      CardBase._dragging_card.draw(screen)