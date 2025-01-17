import time
from random import shuffle
from star_algorithm.index import StarAlgorithm
from bfs.index import ReguaPuzzle

def create_problem(size: int):
  sequence = f'{'B,' * size}{'A,' * size}'
  return sequence.split(',')

size = 9
goal = create_problem(size)
start = goal.copy()
shuffle(start)

start_time = time.perf_counter()

'''
algorithm = StarAlgorithm(tuple(start), tuple(goal), size)
algorithm.run()

algorithm = ReguaPuzzle(start, goal, size)
algorithm.run()
'''

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f'Tempo de execução: {execution_time:.6f} segundos')