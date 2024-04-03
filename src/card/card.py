from typing import Callable, Tuple
from utils.parabola.parabola import Parabola
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
        pygame.draw.rect(
            self.surface, 
            color, 
            (0, 0, self.width, self.height)
        )
        screen.blit(self.surface, (0, 0))
        self.drag(screen)

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

    def drag(self, screen: pygame.Surface):
        if self.is_dragging:
            a = self.surface.get_rect().center
            b = pygame.mouse.get_pos()
            Parabola.draw_parabola(
                screen, 
                a, 
                b, 
                pygame.Color("#ff0000"), 
                5_000_000
            )