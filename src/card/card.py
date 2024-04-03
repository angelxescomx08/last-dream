from typing import Callable
from constants.paths_constants import PATH_CARD_BACKGROUNDS
import pygame

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
        pygame.draw.rect(
            self.surface, 
            color_rgb, 
            (0, 0, self.width, self.height)
        )
        screen.blit(self.surface, (0, 0))
        
    
    def hover(self):
        #el cursor cambia cuando esta sobre la carta
        if self.sub_surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    
    def drag_and_drop(self):
        # Mueve la carta por la pantalla
        if self.sub_surface.get_rect().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            # Actualiza la posición de la superficie con respecto a la posición del ratón
            self.sub_surface.x = pygame.mouse.get_pos()[0] - self.offset_x
            self.sub_surface.y = pygame.mouse.get_pos()[1] - self.offset_y

        
