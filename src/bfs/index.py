from collections import deque

class BFSAlgorithm:
  def __init__(self, start: list, goal: list, size: int):
    self.start = tuple(start)
    self.goal = tuple(goal)
    self.size = size

  def get_neighbors(self, state: tuple):
    empty_position = state.index('')
    neighbors = []

    for distance in range(1, self.size + 1):
      if 0 <= empty_position + distance < len(state):
        neighbor = list(state)
        neighbor[empty_position], neighbor[empty_position + distance] = neighbor[empty_position + distance], neighbor[empty_position]
        neighbors.append(tuple(neighbor))

      if 0 <= empty_position - distance < len(state):
        neighbor = list(state)
        neighbor[empty_position], neighbor[empty_position - distance] = neighbor[empty_position - distance], neighbor[empty_position]
        neighbors.append(tuple(neighbor))

    return neighbors

  def build_path(self, predecessors: dict, end_state: tuple):
    path = []
    current = end_state

    while current in predecessors:
      path.append(list(current))
      current = predecessors[current]

    path.append(list(self.start))
    path.reverse()

    print("Solução:")
    print(*path, sep="\n")
    print(f'Passos: {len(path)}')

  def run(self):
    queue = deque([(self.start, None)])
    visited = set()
    predecessors = {}
    max_memory = nodes_expanded = branches = 0

    while queue:
      max_memory = max(max_memory, len(queue))
      state, parent = queue.popleft()
      nodes_expanded += 1

      if state == self.goal:
        if parent:
          predecessors[state] = parent

        self.build_path(predecessors, state)

        print(f'Nós expandidos: {nodes_expanded}')
        print(f'Máxima memória utilizada: {max_memory}')
        print(f'Fator de ramificação média: {
          branches / nodes_expanded if nodes_expanded > 0 else 0
        }')
        return

      if state not in visited:
        visited.add(state)

        if parent:
          predecessors[state] = parent

        for neighbor in self.get_neighbors(state):
          branches += 1

          if neighbor not in visited:
            queue.append((neighbor, state))

    print("Não foi possível encontrar um final para o algoritmo!")
