# Problema da Mochila - Solução Recursiva
# Complexidade de tempo: O(2^n) — exponencial
# Complexidade de espaço: O(n) — pilha de recursão

import time
def mochila(i, W, pesos, valores):
    chamadas[0] += 1

    """
    Resolve o Problema da Mochila de forma recursiva.

    Parâmetros:
        i (int): índice do item atual (1-indexado)
        W (int): capacidade restante da mochila
        pesos (list): lista de pesos dos itens (índice 1 até n)
        valores (list): lista de valores dos itens (índice 1 até n)

    Retorna:
        int: valor máximo que pode ser obtido
    """
    # Caso base: sem itens ou sem capacidade
    if i == 0 or W == 0:
        return 0

    # Item não cabe na mochila — pula para o anterior
    if pesos[i] > W:
        return mochila(i - 1, W, pesos, valores)

    # Opção 1: usar o item i
    usar = valores[i] + mochila(i - 1, W - pesos[i], pesos, valores)

    # Opção 2: não usar o item i
    nao_usar = mochila(i - 1, W, pesos, valores)

    return max(usar, nao_usar)


# ─── Exemplo de uso ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Itens: (peso, valor)
    itens = [
        (1, 60),
        (3, 150),
        (3, 120),
        (4, 160),
        (5, 200),
        (5, 150),
        (6, 60),
    ]

    n = len(itens)
    capacidade = 10

    # Listas 1-indexadas (índice 0 não é usado)
    pesos   = [0] + [item[0] for item in itens]
    valores = [0] + [item[1] for item in itens]
    chamadas = [0]
    inicio = time.perf_counter()
    resultado = mochila(n, capacidade, pesos, valores)
    fim = time.perf_counter()

    print("=== Problema da Mochila — Solução Recursiva ===")
    print(f"Itens disponíveis : {itens}")
    print(f"Capacidade        : {capacidade}")
    print(f"Valor máximo      : {resultado}")
    print(f"Tempo de execução : {fim - inicio:.6f} segundos")
    print(f"Número de chamadas : {chamadas[0]}")