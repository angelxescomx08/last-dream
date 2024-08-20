from pydantic import BaseModel
from typing import Callable

class CardBase(BaseModel):

  name: str
  cost: int
  description: str
  effect: Callable
