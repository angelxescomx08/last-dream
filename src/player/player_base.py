from abc import abstractmethod
from typing import List
import pygame
from src.game_object.live_character import LiveCharacter
from src.deck.deck import Deck
from src.hand.hand import Hand
from src.piles.pile.pile import Pile


class PlayerBase(LiveCharacter):
    @property
    @abstractmethod
    def hand(self) -> Hand:
        pass

    @property
    @abstractmethod
    def deck(self) -> Deck:
        pass

    @property
    @abstractmethod
    def draw_pile(self) -> Pile:
        pass

    @property
    @abstractmethod
    def discard_pile(self) -> Pile:
        pass

    @property
    @abstractmethod
    def enemies(self) -> List[LiveCharacter]:
        pass

    @property
    @abstractmethod
    def targeted_enemy(self) -> LiveCharacter:
        pass

    def target_enemy(self):
        mouse_pos = pygame.mouse.get_pos()
        if not pygame.mouse.get_pressed()[0]:
            return
        for enemy in self.enemies:
            if enemy.rect.collidepoint(mouse_pos):
                self.targeted_enemy = enemy
                break
            else:
                self.targeted_enemy = None
        for card in self.hand.cards:
            card.targeted_enemy = self.targeted_enemy

    def update(self, screen: pygame.Surface):
        self.target_enemy()
        super().update(screen)
        self.draw_pile.draw_icon_pile(screen, 0, 450)
        self.discard_pile.draw_icon_pile(screen, 750, 450)
        self.hand.draw(screen)
