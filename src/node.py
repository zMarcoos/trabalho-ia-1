class Node:
  def __init__(self, element: tuple, g: int = 0, h: int = 0):
    self.element = element
    self.parent = None
    self.g = g
    self.h = h

  @property
  def f(self):
    return self.g + self.h