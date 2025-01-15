import time
from random import shuffle
from star_algorithm.index import StarAlgorithm

def create_problem(size: int):
  sequence = f'{'A,' * size}{'B,' * size}'
  return sequence.split(',')

size = 7
goal = create_problem(size)
start = goal.copy()
shuffle(start)

start_time = time.perf_counter()

algorithm = StarAlgorithm(tuple(start), tuple(goal), size)
algorithm.run()

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f'Tempo de execução: {execution_time:.6f} segundos')