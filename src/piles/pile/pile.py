from typing import List
from src.piles.base_pile import BasePile
from src.card.card_base import CardBase

class Pile(BasePile):
  cards: List[CardBase] = []
  
  def __init__(self, cards: List[CardBase] = []):
    super().__init__()
    self.cards = cards