from collections import deque
import heapq

class ReguaPuzzle:
  def __init__(self, start: tuple, goal: tuple, size: int):
    self.start = start
    self.goal = goal
    self.size = size

  def h(self, state: tuple):
    return abs(state.index('') - self.goal.index(''))

  def h2(self, state: tuple):
    return sum(1 for a, b in zip(state, self.goal) if a != b)

  def get_neighbors(self, state: tuple):
    empty_position = state.index('')
    neighbors = []

    for distance in range(1, self.size + 1):
      if 0 <= empty_position + distance < len(state):
        neighbor = list(state)
        neighbor[empty_position], neighbor[empty_position + distance] = (
          neighbor[empty_position + distance],
          neighbor[empty_position],
        )
        neighbors.append(tuple(neighbor))

      if 0 <= empty_position - distance < len(state):
        neighbor = list(state)
        neighbor[empty_position], neighbor[empty_position - distance] = (
          neighbor[empty_position - distance],
          neighbor[empty_position],
        )
        neighbors.append(tuple(neighbor))

    return neighbors

  def build_path(self, predecessors: dict, end_state: tuple):
    path = deque()
    current = end_state

    while current in predecessors:
      path.appendleft(list(current))
      current = predecessors[current]

    path.appendleft(list(self.start))

    print("\nSolução encontrada:")
    for step, state in enumerate(path):
      print(f"Passo {step + 1}: {state}")

    print(f'\nTotal de passos: {len(path) - 1}')

  def run(self):
    open_list = []
    heapq.heappush(open_list, (0, self.start))

    g_scores = {self.start: 0}
    predecessors = {}

    closed_list = set()
    branches = 0
    max_memory = 0
    nodes_expanded = 0

    while open_list:
      max_memory = max(max_memory, len(open_list))
      _, current = heapq.heappop(open_list)

      if current == self.goal:
        print(f'\nNós expandidos: {nodes_expanded}')
        print(f'Máxima memória utilizada: {max_memory}')
        print(f'Fator de ramificação média: {
          branches / nodes_expanded if nodes_expanded > 0 else 0:.2f
        }')

        self.build_path(predecessors, current)
        return

      nodes_expanded += 1
      closed_list.add(current)

      for neighbor in self.get_neighbors(current):
        branches += 1
        if neighbor in closed_list: continue

        g = g_scores[current] + 1
        if neighbor not in g_scores or g < g_scores[neighbor]:
          g_scores[neighbor] = g
          f = g + self.h2(neighbor)

          heapq.heappush(open_list, (f, neighbor))
          predecessors[neighbor] = current

    print("\nNenhuma solução encontrada!")
