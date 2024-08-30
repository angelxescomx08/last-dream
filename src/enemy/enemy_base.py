from abc import ABC, abstractmethod

class EnemyBase(ABC):

  @property
  @abstractmethod
  def health(self)->int:
    pass

  @property
  @abstractmethod
  def damage(self)->int:
    pass

  @property
  @abstractmethod
  def position(self)->tuple[int,int]:
    pass