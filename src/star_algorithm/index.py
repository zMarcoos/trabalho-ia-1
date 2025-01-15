class StarAlgorithm:
  def __init__(self, start: tuple, goal: tuple, size: int):
    self.start = start
    self.goal = goal
    self.size = size

  def h(self, from_state: tuple, to_state: tuple):
    return abs(from_state.index('') - to_state.index(''))

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
    begin_g = 0
    begin_h = self.h(self.start, self.goal)

    open_list = {
      self.start: {
        'parent': None,
        'g': begin_g,
        'h': begin_h,
        'f': begin_g + begin_h
      },
    }

    closed_list = {}
    predecessors = {}

    branches = 0
    max_memory = 0
    nodes_expanded = 0

    while len(open_list) != 0:
      max_memory = max(max_memory, len(open_list))
      least_node = min(open_list.items(), key=lambda x: x[1]['f'])

      if least_node[0] == self.goal:
        print(f'Nós expandidos: {nodes_expanded}')
        print(f'Máxima memória utilizada: {max_memory}')
        print(f'Fator de ramificação média: {
          branches / nodes_expanded if nodes_expanded > 0 else 0
        }')

        self.build_path(predecessors, least_node[0])
        return

      nodes_expanded += 1

      open_list.pop(least_node[0])
      closed_list[least_node[0]] = least_node[1]

      for neighbor in self.get_neighbors(least_node[0]):
        branches += 1

        if neighbor in closed_list: continue

        calculated_g = least_node[1]['g'] + 1
        if neighbor in open_list:
          if calculated_g >= open_list[neighbor]['g']: continue

        h = self.h(neighbor, self.goal)
        open_list[neighbor] = {
          'parent': least_node[0],
          'g': calculated_g,
          'h': h,
          'f': calculated_g + h
        }

        predecessors[neighbor] = least_node[0]

    print('Sem solução!')
