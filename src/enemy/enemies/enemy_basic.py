from src.enemy.enemy_base import EnemyBase
import pygame

class EnemyBasic(EnemyBase,pygame.sprite.Sprite):

  health: int = 100
  damage: int = 10
  position: tuple[int,int] = (0,0)

  def __init__(self):
    super().__init__()
    
    
