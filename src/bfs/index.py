from collections import deque

class ReguaPuzzle:
  def __init__(self, inicio, meta, tamanho: int):
    self.tamanho = tamanho
    self.inicio = inicio
    self.meta = meta

  def gerar_sucessores(self, estado):
    sucessores = []
    vazio = estado.index("")

    for deslocamento in range(-self.tamanho, self.tamanho + 1):
      i = vazio + deslocamento
      if 0 <= i < len(estado) and estado[i] != "":
        novo_estado = estado[:]
        novo_estado[vazio], novo_estado[i] = novo_estado[i], novo_estado[vazio]

        if novo_estado != estado:
          sucessores.append((novo_estado, abs(deslocamento)))

    return sucessores

  def verificar_objetivo(self, estado):
    return estado == self.meta

  def run(self):
    fila = deque([(self.inicio, 0, [])])
    visitados = set()
    max_memoria = 0
    nos_expandidos = 0
    total_filhos = 0
    nos_internos = 0

    while fila:
      max_memoria = max(max_memoria, len(fila))
      estado, custo, caminho = fila.popleft()

      if self.verificar_objetivo(estado):
        fator_ramificacao = total_filhos / nos_internos if nos_internos > 0 else 0
        caminho = caminho + [estado]

        print("\nSolução encontrada:")

        for indice, estado in enumerate(caminho):
          print(f"Passo {indice + 1}: {estado}")

        print(f'Quantidade de passos: {len(caminho) + 1}')
        print(f"Custo total: {custo}")
        print(f"Memória máxima utilizada: {max_memoria}")
        print(f"Nós expandidos: {nos_expandidos}")
        print(f"Fator de ramificação médio: {fator_ramificacao}")
        return

      visitados.add(tuple(estado))
      filhos = 0

      for sucessor, custo_movimento in self.gerar_sucessores(estado):
        if tuple(sucessor) not in visitados:
          visitados.add(tuple(sucessor))
          fila.append((sucessor, custo + custo_movimento, caminho + [estado]))
          filhos += 1

      if filhos > 0:
        nos_internos += 1
        total_filhos += filhos

      nos_expandidos += 1

    print('Sem solução')
