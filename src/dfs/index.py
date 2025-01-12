import random
import time

def gerador_de_estado_inicial(N):
    blocos = ['B'] * N + ['A'] * N
    random.shuffle(blocos)
    pos_vazio = N
    estado_inicial = blocos[:pos_vazio] + ['-'] + blocos[pos_vazio:]
    print("Estado inicial:", estado_inicial)
    return estado_inicial

def gerador_de_sucessores(estado, N):
    sucessores = []
    pos_vazio = estado.index('-')

    for i in range(len(estado)):
        if abs(pos_vazio - i) <= N and estado[i] != '-':
            novo_estado = estado.copy()
            novo_estado[pos_vazio], novo_estado[i] = novo_estado[i], novo_estado[pos_vazio]
            sucessores.append(novo_estado)
    return sucessores

def verificar_objetivo(estado):
    encontrou_azul = False
    for bloco in estado:
        if bloco == 'A':
            encontrou_azul = True
        if bloco == 'B' and encontrou_azul:
            return False
    return True

def busca_limitada(estado, limite, N, nos_expandidos, memoria_maxima):
    nos_expandidos[0] += 1
    memoria_maxima[0] = max(memoria_maxima[0], limite)

    if verificar_objetivo(estado):
        return [estado]

    if limite == 0:
        return None

    for sucessor in gerador_de_sucessores(estado, N):
        resultado = busca_limitada(sucessor, limite - 1, N, nos_expandidos, memoria_maxima)
        if resultado:
            return [estado] + resultado
    return None

def iddfs(estado_inicial, profundidade_maxima, N):
    for limite in range(profundidade_maxima + 1):
        nos_expandidos = [0]
        memoria_maxima = [0]
        resultado = busca_limitada(estado_inicial, limite, N, nos_expandidos, memoria_maxima)
        if resultado:
            return resultado, nos_expandidos[0], memoria_maxima[0]
    return None, nos_expandidos[0], memoria_maxima[0]

def main():
    N = 10
    estado_inicial = gerador_de_estado_inicial(N)
    profundidade_maxima = 10

    inicio = time.time()
    resultado, nos_expandidos, memoria_maxima = iddfs(estado_inicial, profundidade_maxima, N)
    fim = time.time()

    if resultado:
        print("\nSolução encontrada:")
        for idx, estado in enumerate(resultado):
            print(f"Passo {idx + 1}: {estado}")
        print(f"\nTempo total: {fim - inicio:.4f} segundos")
        print(f"Nós expandidos: {nos_expandidos}")
        print(f"Memória máxima usada (profundidade): {memoria_maxima}")
        print(f"Quantidade de passos: {len(resultado) - 1}")
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()
