from src.card.card_base import CardBase
from src.hand.hand_base import HandBase
from typing import List


class Hand(HandBase):

    cards: List[CardBase] = []

    def __init__(self, cards: List[CardBase] = []):
        super().__init__()
        self.cards = cards
        for i, card in enumerate(self.cards):
            card.position = (i * 100 + i * 20, 450)
            card.initial_position = card.position

    def add_card(self, card: CardBase):
        self.cards.append(card)

    def remove_card(self, card: CardBase):
        self.cards.remove(card)
