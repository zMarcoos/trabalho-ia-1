from collections import deque

class ReguaPuzzle:
    def __init__(self, estado_inicial, n):
        self.estado_inicial = estado_inicial
        self.n = n
        self.posicao_meta = [("B" if i < n else "A") for i in range(2 * n)] + ["-"]

    def encontrar_vazio(self, estado):
        return estado.index("-")

    def gerar_sucessores(self, estado):
        vazio = self.encontrar_vazio(estado)
        sucessores = []
        for i in range(max(0, vazio - self.n), min(len(estado), vazio + self.n + 1)):
            if i != vazio:
                novo_estado = estado[:]
                novo_estado[vazio], novo_estado[i] = novo_estado[i], novo_estado[vazio]
                sucessores.append((novo_estado, abs(vazio - i)))
        return sucessores

    def estado_final(self, estado):
        return estado == self.posicao_meta

    def bfs(self):
        fila = deque([(self.estado_inicial, 0, [])])
        visitados = set()

        while fila:
            estado, custo, caminho = fila.popleft()
            if self.estado_final(estado):
                return caminho + [estado], custo

            visitados.add(tuple(estado))

            for sucessor, custo_mov in self.gerar_sucessores(estado):
                if tuple(sucessor) not in visitados:
                    fila.append((sucessor, custo + custo_mov, caminho + [estado]))

    


# Exemplo de uso:
n = 2
estado_inicial = ["B", "A", "-", "A", "B"]
puzzle = ReguaPuzzle(estado_inicial, n)

print("BFS:")
caminho, custo = puzzle.bfs()
for passo in caminho:
    print(passo)
print("Custo total:", custo)