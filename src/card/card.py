from typing import Callable
from constants.paths_constants import PATH_CARD_BACKGROUNDS
import pygame
import os

class Card:
    image: str
    mana: int
    effect: Callable
    sprite_sheet_path: str
    surface: pygame.Surface
    sub_surface: pygame.Surface

    def __init__(self, image: str, mana: int, effect: Callable):
        self.image = image
        self.mana = mana
        self.effect = effect
        self.load_sprite()
    
    def load_sprite(self) -> None:
        self.sprite_sheet_path = os.path.join(
            PATH_CARD_BACKGROUNDS
        )
        self.surface = pygame.image.load(self.sprite_sheet_path)
        # Tomar la porción de la imagen deseada (columna 8, fila 1)
        ancho_celda = self.surface.get_width() // 8
        alto_celda = self.surface.get_height() // 3
        columna = 7  # Índice 7 para la columna 8 (se empieza desde 0)
        fila = 1     # Índice 0 para la fila 1

        # Extraer la porción deseada de la imagen
        self.sub_surface = self.surface.subsurface(
            (columna * ancho_celda, fila * alto_celda, ancho_celda, alto_celda)
        )

    def draw(self):
        #pinta la carta en la pantalla usando el fondo de la carta
        self.hover()
        self.drag_and_drop()
        return self.sub_surface
    
    def hover(self):
        #el cursor cambia cuando esta sobre la carta
        if self.sub_surface.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    
    def drag_and_drop(self):
        #mueve la carta por la pantalla
        if self.sub_surface.get_rect().collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.sub_surface.get_rect().x = pygame.mouse.get_pos()[0]
            self.sub_surface.get_rect().y = pygame.mouse.get_pos()[1]

        
