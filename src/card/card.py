from typing import Callable, Tuple
from constants.paths_constants import PATH_CARD_BACKGROUNDS
import pygame

class Card:
    image: str
    mana: int
    effect: Callable
    surface: pygame.Surface
    width: int = 100
    height: int = 150

    is_dragging: bool = False
    is_hovering: bool = False

    def __init__(self, image: str, mana: int, effect: Callable):
        self.image = image
        self.mana = mana
        self.effect = effect  
        self.surface = pygame.Surface((self.width, self.height)) 

    def draw(self, screen: pygame.Surface):
        self.detect_hover()
        self.detect_drag()
        color = self.hover()
        position = self.drag()
        pygame.draw.rect(
            self.surface, 
            color, 
            (0, 0, self.width, self.height)
        )
        screen.blit(self.surface, position)

    def detect_hover(self):
        # el cursor cambia cuando está sobre la carta
        if self.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            self.is_hovering = True
        else:
            self.is_hovering = False
    
    def hover(self):
        color = pygame.Color("#ffffff")
        if self.is_hovering and not self.is_dragging:  # Solo cambia el color si no está siendo arrastrada
            color = pygame.Color("#ff0000")
        return color
            
    
    def detect_drag(self):
        # detecta si el mouse está sobre la carta
        if not pygame.mouse.get_pressed()[0]:
            self.is_dragging = False
        elif self.is_hovering and pygame.mouse.get_pressed()[0]:
            self.is_dragging = True

    def drag(self) -> Tuple[int, int]:
        # Mueve la carta por la pantalla
        if self.is_dragging:
            x, y = pygame.mouse.get_pos()
            return (x - self.width // 2, y - self.height // 2)
        else:
            return [0, 0]