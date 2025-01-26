from abc import abstractmethod

from pygame import Surface
import pygame
from src.game_object.animated_object import AnimatedObject


class LiveCharacter(AnimatedObject):

    @property
    @abstractmethod
    def health(self) -> int:
        pass

    @property
    @abstractmethod
    def max_health(self) -> int:
        pass

    @property
    @abstractmethod
    def damage(self) -> int:
        pass

    def draw_heatlh(self, screen: Surface):
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.health}/{self.max_health}", True, (255, 255, 255))
        center = (self.rect.centerx - text.get_width() // 2, self.position[1] - 30)
        screen.blit(text, center)

    def update(self, screen: Surface):
        super().update(screen)
        self.draw_heatlh(screen)
