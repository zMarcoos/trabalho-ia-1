from star_algorithm.priority_queue import PriorityQueue

class StarAlgorithm:
  def __init__(self, start: list, goal: list, size: int):
    self.start = tuple(start)
    self.goal = tuple(goal)
    self.size = size

  def moviment_cost(self, state: tuple, neighbor: tuple):
    return abs(state.index('') - neighbor.index(''))

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

  def first_heuristic(self, state: tuple):
    return sum(1 for a, b in zip(state, self.goal) if a != b)

  def second_heuristic(self, state: tuple):
    goal_positions = { value: index for index, value in enumerate(self.goal) }
    return sum(
      abs(index - goal_positions[item]) for index, item in enumerate(state) if item != ''
    )

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
    possibilities = PriorityQueue()
    possibilities.insert(0, self.start)

    g_costs = { self.start: 0 }
    predecessors = {}

    branches = 0
    max_memory = 0
    nodes_expanded = 0

    while not possibilities.empty():
      max_memory = max(max_memory, len(possibilities.queue))

      _, state = possibilities.remove()
      nodes_expanded += 1

      if state == self.goal:
        self.build_path(predecessors, state)
        print(f'Nós expandidos: {nodes_expanded}')
        print(f'Máxima memória utilizada: {max_memory}')
        print(f'Fator de ramificação média: {
          branches / nodes_expanded if nodes_expanded > 0 else 0
        }')
        return

      for neighbor in self.get_neighbors(state):
        branches += 1
        calculated_g_cost = g_costs[state] + self.moviment_cost(state, neighbor)

        if neighbor not in g_costs or calculated_g_cost < g_costs[neighbor]:
          g_costs[neighbor] = calculated_g_cost
          f_cost = calculated_g_cost + self.first_heuristic(neighbor)

          possibilities.insert(f_cost, neighbor)
          predecessors[neighbor] = state

    print("Não foi possível encontrar um final para o algoritmo!")
