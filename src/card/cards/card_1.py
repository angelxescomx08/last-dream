from src.card.card_base import CardBase

class AttackCard(CardBase):
  is_hovered: bool = False
  is_dragged: bool = False
  position: tuple[int,int] = (0, 0)
  name: str = "Attack"
  cost: int = 1
  description: str = "Deal 5 damage"

  def __init__(self):
    super().__init__()

  def effect(self):
    pass

  def play(self):
    pass

  def hover(self):
    pass

  def drag(self):
    pass

  def draw(self):
    pass
