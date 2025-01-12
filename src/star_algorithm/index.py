from priority_queue import PriorityQueue

size = 2
start = ['B', 'A', 'B', 'A', '']
goal =['B', 'B', '', 'A', 'A']

def moviment_cost(state, neighbor):
  return abs(state.index('') - neighbor.index(''))

def get_neighbors(state):
  empty_postion = state.index('')
  neighbors = []

  for distance in range(1, size + 1):
    if 0 < empty_postion + distance < len(state):
      neighbor = state[:]
      neighbor[empty_postion], neighbor[empty_postion + distance] = neighbor[empty_postion + distance], neighbor[empty_postion]
      neighbors.append(neighbor)

    if 0 < empty_postion - distance < len(state):
      neighbor = state[:]
      neighbor[empty_postion], neighbor[empty_postion - distance] = neighbor[empty_postion - distance], neighbor[empty_postion]
      neighbors.append(neighbor)

  return neighbors

def heuristic(state):
  return sum(1 for a, b in zip(state, goal) if a != b)

def other_heuristic(state):
  return sum(abs(state.index(item) - goal.index(item)) for item in state if item != '')

def star_algorithm():
  possibilities: PriorityQueue = PriorityQueue()
  possibilities.insert(0, start)

  g_costs = { str(start): 0 }

  path = {}

  while not possibilities.empty():
    _, state = possibilities.remove()

    if state == goal:
      return path

    for neighbor in get_neighbors(state):
      calculated_g_cost = g_costs[str(state)] + moviment_cost(state, neighbor)

      if str(neighbor) not in g_costs or calculated_g_cost < g_costs[str(neighbor)]:
        g_costs[str(neighbor)] = calculated_g_cost
        f_cost = calculated_g_cost + heuristic(neighbor)

        possibilities.insert(f_cost, neighbor)
        path[str(neighbor)] = state

  return None

path = star_algorithm()
if path:
  print('Solução:')
  for moviment in path:
    print(moviment)
else:
  print('Não foi possível encontrar um final para o algoritmo!')