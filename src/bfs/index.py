import random
import time
from collections import deque

class ReguaPuzzle:
    def __init__(self, N):
        self.N = N
        self.estado_inicial = self.gerador_de_estado_inicial()
        self.posicao_meta = ["B" if i < N else "A" for i in range(2 * N)] + ["-"]

    def gerador_de_estado_inicial(self):
        blocos = ["B"] * self.N + ["A"] * self.N
        random.shuffle(blocos)
        pos_vazio = self.N
        estado_inicial = blocos[:pos_vazio] + ["-"] + blocos[pos_vazio:]
        print("Estado inicial:", estado_inicial)
        return estado_inicial

    def gerar_sucessores(self, estado):
        sucessores = []
        vazio = estado.index("-")
        # Gera os índices válidos para troca (dentro dos limites e respeitando as regras)
        for deslocamento in range(-self.N, self.N + 1):
            i = vazio + deslocamento
            if 0 <= i < len(estado) and estado[i] != "-":
                novo_estado = estado.copy()
                novo_estado[vazio], novo_estado[i] = novo_estado[i], novo_estado[vazio]
                sucessores.append(novo_estado)
        return sucessores

    def verificar_objetivo(self, estado):
        encontrou_azul = False
        for bloco in estado:
            if bloco == "A":
                encontrou_azul = True
            if bloco == "B" and encontrou_azul:
                return False
        return True


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

            if self.verificar_objetivo(estado):
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

            for sucessor in self.gerar_sucessores(estado):
                if tuple(sucessor) not in visitados:
                    visitados.add(tuple(sucessor))
                    fila.append((sucessor, custo + 1, caminho + [estado]))


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

def main():
    N = 4
    puzzle = ReguaPuzzle(N)

    inicio = time.time()
    resultado = puzzle.bfs()
    fim = time.time()

    if resultado["caminho"]:
        print("\nSolução encontrada:")
        for idx, estado in enumerate(resultado["caminho"]):
            print(f"Passo {idx + 1}: {estado}")
        print(f"\nTempo total: {fim - inicio:.4f} segundos")
        print(f"Custo total: {resultado['custo_total']}")
        print(f"Quantidade de passos: {resultado['passos']}")
        print(f"Memória máxima utilizada: {resultado['max_memoria']}")
        print(f"Nós expandidos: {resultado['nos_expandidos']}")
        print(f"Fator de ramificação médio: {resultado['fator_ramificacao']}")
    else:
        print("Nenhuma solução encontrada.")
        print(f"Tempo total: {fim - inicio:.4f} segundos")
        print(f"Memória máxima utilizada: {resultado['max_memoria']}")
        print(f"Nós expandidos: {resultado['nos_expandidos']}")
        print(f"Fator de ramificação médio: {resultado['fator_ramificacao']}")

if __name__ == "__main__":
    main()
