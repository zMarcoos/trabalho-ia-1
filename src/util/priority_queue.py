import heapq

class PriorityQueue:
  def __init__(self):
    self.queue: list = []
    self.size: int = 0

  def insert(self, priority: int, element: list):
    heapq.heappush(self.queue, (priority, element))
    self.size += 1

  def remove(self):
    self.size -= 1
    return heapq.heappop(self.queue)

  def contains(self, item: tuple):
    return item in self.queue

  def empty(self):
    return len(self.queue) == 0