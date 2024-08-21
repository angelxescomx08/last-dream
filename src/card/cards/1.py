from src.card.card_base import Card

class AttackCard(Card):
  def __init__(self):
    super().__init__()
    self.name = 'Attack'
    self.description = 'Deals 5 damage to the enemy'
    self.cost = 1
    self.damage = 5

  def play(self, player, opponent):
    super().play(player, opponent)
    opponent.health -= self.damage