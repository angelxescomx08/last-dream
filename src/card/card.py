from typing import Callable
from constants.paths_constants import PATH_CARD_BACKGROUNDS
import pygame
from typing import List

class Card:
    image: str
    mana: int
    effect: Callable
    surface: pygame.Surface
    width: int = 100
    height: int = 150

    def __init__(self, image: str, mana: int, effect: Callable):
        self.image = image
        self.mana = mana
        self.effect = effect  
        self.surface = pygame.Surface((self.width, self.height)) 

    def draw(self, screen: pygame.Surface):
        color_rgb = pygame.Color("#ffffff")
        self.hover()
        position = self.drag_and_drop()
        pygame.draw.rect(
            self.surface, 
            color_rgb, 
            (0, 0, self.width, self.height)
        )
        screen.blit(self.surface, position)
        
    
    def hover(self):
        #el cursor cambia cuando esta sobre la carta
        if self.surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            self.height *= 1.2 
            self.width *= 1.2
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        else:
            self.height /= .8
            self.width /= .8
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    
    def drag_and_drop(self) -> List[int]:
        # Mueve la carta por la pantalla
        if self.surface.get_rect().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return pygame.mouse.get_pos()
        else:
            return [0, 0]

        
