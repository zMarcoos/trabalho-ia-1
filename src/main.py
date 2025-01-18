import time
from random import shuffle
from star_algorithm.index import ReguaPuzzle
#from bfs.index import ReguaPuzzle
#from dfs.index import ReguaPuzzle

def create_problem(size: int):
  sequence = f'{'B,' * size}{'A,' * size}'
  return sequence.split(',')

size = 10
goal = create_problem(size)
start = goal.copy()
shuffle(start)

start_time = time.perf_counter()

'''
algorithm = ReguaPuzzle(tuple(start), tuple(goal), size)
algorithm.run()

algorithm = ReguaPuzzle(start, goal, size)
algorithm.run()

algorithm = ReguaPuzzle(start, goal, size)
algorithm.run()
'''

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f'Tempo de execução: {execution_time:.6f} segundos')
