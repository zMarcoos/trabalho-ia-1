from collections import deque

class ReguaPuzzle:
    def __init__(self, inicial, meta, tamanho):
        self.tamanho = tamanho
        self.inicial = inicial
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

    def busca_limitada(self, limite):
        pilha = deque([(self.inicial, 0, [])])
        visitados = set()
        nos_expandidos = 0
        memoria_maxima = 0
        total_filhos = 0
        nos_internos = 0

        while pilha:
            memoria_maxima = max(memoria_maxima, len(pilha))
            estado, profundidade, caminho = pilha.pop()

            if self.verificar_objetivo(estado):
                fator_ramificacao = total_filhos / nos_internos if nos_internos > 0 else 0
                return caminho + [estado], nos_expandidos, memoria_maxima, fator_ramificacao

            if profundidade < limite:
                nos_expandidos += 1
                visitados.add(tuple(estado))

                sucessores = self.gerar_sucessores(estado)
                filhos_atuais = 0

                for sucessor, _ in sucessores:
                    if tuple(sucessor) not in visitados:
                        pilha.append((sucessor, profundidade + 1, caminho + [estado]))
                        filhos_atuais += 1

                if filhos_atuais > 0:
                    total_filhos += filhos_atuais
                    nos_internos += 1

        fator_ramificacao = total_filhos / nos_internos if nos_internos > 0 else 0
        return None, nos_expandidos, memoria_maxima, fator_ramificacao

    def iddfs(self, profundidade_maxima):
        for limite in range(profundidade_maxima + 1):
            resultado, nos_expandidos, memoria_maxima, fator_ramificacao = self.busca_limitada(limite)
            if resultado:
                return resultado, nos_expandidos, memoria_maxima, fator_ramificacao

        return None, nos_expandidos, memoria_maxima, 0

    def run(self, profundidade_maxima=15):
        resultado, nos_expandidos, memoria_maxima, fator_ramificacao = self.iddfs(profundidade_maxima)

        if resultado:
            print("\nSolução encontrada:")
            for indice, estado in enumerate(resultado):
                print(f"Passo {indice + 1}: {estado}")

            print(f"\nNós expandidos: {nos_expandidos}")
            print(f"Memória máxima usada (profundidade): {memoria_maxima}")
            print(f"Quantidade de passos: {len(resultado) - 1}")
            print(f"Fator de ramificação médio: {fator_ramificacao:.2f}")
        else:
            print("\nNenhuma solução encontrada.")
