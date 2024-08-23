from abc import ABC
from typing import List

from card.card_base import CardBase


class DeckBase(ABC):

  @property
  def cards(self) -> List[CardBase]:
    pass
