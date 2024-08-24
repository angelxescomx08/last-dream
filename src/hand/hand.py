from src.card.card_base import CardBase
from src.hand.hand_base import HandBase
from typing import List

class Hand(HandBase):

  cards: List[CardBase]

  def __init__(self, cards: List[CardBase] = []):
    self.cards = cards

  @property
  def cards(self) -> List[CardBase]:
    return self._cards

  def add_card(self, card: CardBase):
    self.cards.append(card)

  def remove_card(self, card: CardBase):
    self.cards.remove(card)