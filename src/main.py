import time
from random import shuffle
from star_algorithm.index import StarAlgorithm
from bfs.index import BFSAlgorithm
from dfs.index import DFSAlgorithm

def create_problem(size: int):
  sequence = f'{'A,' * size}{'B,' * size}'
  return sequence.split(',')

size = 10
goal = create_problem(size)
start = goal.copy()
shuffle(start)

start_time = time.perf_counter()

'''
algorithm = StarAlgorithm(start, goal, size)
algorithm.run()

algorithm = BFSAlgorithm(start, goal, size)
algorithm.run()
'''

algorithm = DFSAlgorithm(start, goal, size)
algorithm.run(6)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f'Tempo de execução: {execution_time:.6f} segundos')