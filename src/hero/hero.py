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
        self.current_tick = 0
        self.sprite_width, self.sprite_height = 64,64
        self.x, self.y = 0, 64*7
        self.position = [0,0]
        self.current_frame = 0
        self.columns = 10  # Número de columnas en la hoja de sprites
        self.delay = 50

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
        self.current_tick = (self.current_tick + 1)%self.delay

        #reducir la cantidad de frames por segundo
        if self.current_tick % (self.delay/self.columns) == 0:    
            self.current_frame = (self.current_frame + 1) % self.columns

        self.x = self.current_frame * self.sprite_width
        self.screen.blit(
            self.hero_sprite, 
            self.position, 
            (self.x, self.y, self.sprite_width, self.sprite_height)
        )

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed

        