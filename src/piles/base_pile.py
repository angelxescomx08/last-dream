from abc import ABC, abstractmethod
from typing import List

from pygame import Surface
from src.card.card_base import CardBase


class BasePile(ABC):
    @property
    @abstractmethod
    def cards(self) -> List[CardBase]:
        pass

    def draw_icon_pile(self, screen: Surface, x: int, y: int) -> None:
        rectangle = Surface((50, 75))
        rectangle.fill((255, 255, 255))
        screen.blit(rectangle, (x, y))

    def add_card(self, card: CardBase) -> None:
        self.cards.append(card)

    def remove_card(self) -> CardBase:
        return self.cards.pop()
