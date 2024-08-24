from abc import ABC, abstractmethod
from typing import List

from card.card_base import CardBase


class DeckBase(ABC):

  @property
  @abstractmethod
  def cards(self) -> List[CardBase]:
    pass
