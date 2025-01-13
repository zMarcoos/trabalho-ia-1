from collections import deque
import time

class ReguaPuzzle:
    def __init__(self, estado_inicial, n):
        self.estado_inicial = estado_inicial
        self.n = n
        self.posicao_meta = ["B" if i < n else "A" for i in range(2 * n)] + ["-"]

    def encontrar_vazio(self, estado):
        return estado.index("-")

    def gerar_sucessores(self, estado):
        vazio = self.encontrar_vazio(estado)
        sucessores = []
        for i in range(max(0, vazio - self.n), min(len(estado), vazio + self.n + 1)):
            if i != vazio:
                novo_estado = estado[:]
                novo_estado[vazio], novo_estado[i] = novo_estado[i], novo_estado[vazio]
                sucessores.append((novo_estado, abs(vazio - i)))  # Retorna o estado e o custo do movimento
        return sucessores

    def estado_final(self, estado):
        return estado == self.posicao_meta

    def bfs(self):
        fila = deque([(self.estado_inicial, 0, [])])  # (estado, custo, caminho)
        visitados = set()
        max_memoria = 0
        nos_expandidos = 0
        total_filhos = 0
        nos_internos = 0

        inicio_tempo = time.time()

        while fila:
            max_memoria = max(max_memoria, len(fila))
            estado, custo, caminho = fila.popleft()

            if self.estado_final(estado):
                tempo_total = time.time() - inicio_tempo
                fator_ramificacao = total_filhos / nos_internos if nos_internos > 0 else 0
                return {
                    "caminho": caminho + [estado],
                    "custo_total": custo,
                    "passos": len(caminho) + 1,
                    "tempo": tempo_total,
                    "max_memoria": max_memoria,
                    "nos_expandidos": nos_expandidos,
                    "fator_ramificacao": fator_ramificacao
                }

            visitados.add(tuple(estado))
            filhos = 0

            for sucessor, custo_mov in self.gerar_sucessores(estado):
                if tuple(sucessor) not in visitados:
                    fila.append((sucessor, custo + custo_mov, caminho + [estado]))
                    filhos += 1

            if filhos > 0:
                nos_internos += 1
                total_filhos += filhos

            nos_expandidos += 1

        tempo_total = time.time() - inicio_tempo
        return {
            "caminho": None,
            "custo_total": None,
            "passos": None,
            "tempo": tempo_total,
            "max_memoria": max_memoria,
            "nos_expandidos": nos_expandidos,
            "fator_ramificacao": 0
        }

# Exemplo de uso:
n = 2
estado_inicial = ["B", "A", "-", "A", "B"]
puzzle = ReguaPuzzle(estado_inicial, n)

resultado = puzzle.bfs()

if resultado["caminho"]:
    print("Caminho da solução:")
    for passo in resultado["caminho"]:
        print(passo)
    print("Custo total:", resultado["custo_total"])
    print("Quantidade de passos:", resultado["passos"])
    print("Tempo gasto:", resultado["tempo"], "segundos")
    print("Memória máxima utilizada:", resultado["max_memoria"])
    print("Nós expandidos:", resultado["nos_expandidos"])
    print("Fator de ramificação médio:", resultado["fator_ramificacao"])
else:
    print("Nenhuma solução encontrada.")
    print("Tempo gasto:", resultado["tempo"], "segundos")
    print("Memória máxima utilizada:", resultado["max_memoria"])
    print("Nós expandidos:", resultado["nos_expandidos"])
    print("Fator de ramificação médio:", resultado["fator_ramificacao"])
