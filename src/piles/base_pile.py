from abc import ABC, abstractmethod
from typing import List
from src.card.card_base import CardBase


class BasePile(ABC):
    @property
    @abstractmethod
    def cards(self) -> List[CardBase]:
        pass

    def add_card(self, card: CardBase) -> None:
        self.cards.append(card)

    def remove_card(self) -> CardBase:
        return self.cards.pop()
