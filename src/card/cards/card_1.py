from typing import List
import pygame
from src.card.card_base import CardBase
from src.game_object.live_character import LiveCharacter

class AttackCard(CardBase):
  screen: pygame.Surface
  rect: pygame.Rect = pygame.Rect(0, 0, 100, 150)
  is_hovered: bool = False
  is_dragged: bool = False
  initial_position: tuple[int,int] = (0, 0)
  position: tuple[int,int] = (0, 0)
  name: str = "Attack"
  cost: int = 1
  description: str = "Deal 5 damage"

  player: LiveCharacter = None
  enemies: List[LiveCharacter] = []
  targeted_enemy: LiveCharacter = None

  def __init__(
    self, 
    screen: pygame.Surface, 
    position: tuple[int,int] = (0, 0),
    player: LiveCharacter = None,
    enemies: List[LiveCharacter] = [],
    targeted_enemy: LiveCharacter = None
  ):
    super().__init__()
    self.screen = screen
    self.rect = pygame.Rect(0, 0, 100, 150)
    self.is_hovered = False
    self.is_dragged = False
    self.position = position
    self.initial_position = position
    self.name = "Attack"
    self.cost = 1
    self.description = "Deal 5 damage"
    self.player = player
    self.enemies = enemies
    self.targeted_enemy = targeted_enemy

  def effect(
    self, 
    player: LiveCharacter, 
    enemies: List[LiveCharacter],
    targeted_enemy: LiveCharacter
  ):
    # if targeted_enemy:
    #   targeted_enemy.health -= player.damage+5
    for enemy in enemies:
      enemy.health -= player.damage+5
      print(f"Enemy health: {enemy.health}")
    
    
