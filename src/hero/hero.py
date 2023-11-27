import pygame
import os

class Hero:
    def __init__(self, screen: pygame.Surface,current_directory: str) -> None:
        self.health = 100
        self.max_health = 100
        self.speed = 5
        self.position = [0, 0]
        self.hero_sprite = None
        self.screen = screen

        self.sprite_width, self.sprite_height = 64,64
        self.x, self.y = 0, 64*7
        self.position = [0,0]
        self.current_frame = 0
        self.columns = 10  # Número de columnas en la hoja de sprites

        self.load_sprites(current_directory)
    
    def load_sprites(self, current_directory: str) -> None:
        # Construir la ruta completa al archivo
        sprite_sheet_path = os.path.join(
            current_directory,
            'assets/hero/hero.png'
        )
        if not os.path.exists(sprite_sheet_path):
            raise FileNotFoundError(
                f"No se encontró el archivo: {sprite_sheet_path}"
            )
        self.hero_sprite = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.hero_sprite = pygame.transform.scale2x(self.hero_sprite)
        

    def animate(self) -> None:
        #animar imagen de 320x320 con 10 frames de 32x32
        self.current_frame = (self.current_frame + 1) % self.columns
        self.x = self.current_frame * self.sprite_width
        self.screen.blit(
            self.hero_sprite, 
            self.position, 
            (self.x, self.y, self.sprite_width, self.sprite_height)
        )
        