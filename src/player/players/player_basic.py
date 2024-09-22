import os
import pygame
from src.player.player_base import PlayerBase
from src.card.cards.card_1 import AttackCard
from src.deck.deck import Deck
from src.hand.hand import Hand
from src.game_object.live_character import LiveCharacter
from typing import List

class PlayerBasic(PlayerBase):
  health: int = 100
  max_health: int = 100
  position: tuple[int, int] = (0, 0)
  current_frame: int = 0
  frame_rate: int = 100
  sprites: List[pygame.Surface] = []
  last_update: int = 0
  hand: Hand = Hand()
  deck: Deck = Deck()
  damage: int = 10

  enemies: List[LiveCharacter] = []
  targeted_enemy: LiveCharacter = None

  def __init__(
    self, 
    position: tuple[int, int], 
    enemies: List[LiveCharacter] = []
  ):
    super().__init__()
    self.position = position
    # Tiempo de la última actualización
    self.last_update = pygame.time.get_ticks() 

    # Obtener la ruta absoluta del directorio actual (enemy_basic.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta correcta hacia el sprite (retrocedemos dos niveles)
    sprite_path = os.path.join(
      current_dir, 
      "../../../assets/heroes/hero_girl/hero_girl.png",
    ) 

    # Llamar al método estático load_sprite
    self.sprites = self.load_sprite(
      sprite_path, 
      (320, 320), 
      (10, 10), 
      row_to_animate=0,
      iterate_all=False, 
      flipped=False,
      scale_factor=2
    )
    
    self.enemies = enemies
    
    cards = [
      AttackCard(
        pygame.display.get_surface(),
        position=(0,0),
        player=self,
        enemies=self.enemies,
        targeted_enemy=self.targeted_enemy
      ) 
      for _ in range(5)
    ]
    
    self.hand = Hand(cards)
    
  def update(self, screen: pygame.Surface):
    # Actualizar el sprite actual
    self.target_enemy()
    super().update(screen)
    self.hand.draw(screen)