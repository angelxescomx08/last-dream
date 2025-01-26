from typing import List
import pygame
from src.player.players.player_basic import PlayerBasic
from src.enemy.enemies.enemy_basic import EnemyBasic
from src.game_object.live_character import LiveCharacter


class Game:
    pygame
    screen: pygame.Surface
    clock: pygame.time.Clock
    running: bool
    current_frame: int

    player: LiveCharacter = None
    enemies: List[LiveCharacter] = []

    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((800, 600))
        self.pygame.display.set_caption("Last dream")
        self.clock = self.pygame.time.Clock()
        self.running = True

        self.enemies = [
            EnemyBasic((650, 200)),
            EnemyBasic((450, 200)),
        ]
        self.player = PlayerBasic((100, 250), self.enemies)

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.running = False
            self.pygame.display.update()
            self.screen.fill((0, 0, 0))
            for enemy in self.enemies:
                enemy.update(self.screen)
            self.player.update(self.screen)
        self.pygame.quit()
        quit()
