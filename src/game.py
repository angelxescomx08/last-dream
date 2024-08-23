import pygame
from src.card.cards.card_1 import AttackCard

card_1 = AttackCard()

class Game:
  pygame
  screen: pygame.Surface
  clock: pygame.time.Clock
  running: bool

  def __init__(self):
    self.pygame = pygame
    self.pygame.init()
    self.screen = self.pygame.display.set_mode((800, 600))
    self.pygame.display.set_caption("Last dream")
    self.clock = self.pygame.time.Clock()
    self.running = True

  def run(self):
    while self.running:
      self.clock.tick(60)
      for event in self.pygame.event.get():
        if event.type == self.pygame.QUIT:
          self.running = False
      self.pygame.display.update()
      card_1.draw()
    self.pygame.quit()
    quit()