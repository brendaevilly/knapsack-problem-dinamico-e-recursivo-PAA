# Problema da Mochila - Programação Dinâmica

import time

def mochila_pd(W, pesos, valores, n, chamadas):

    # cria matriz
    M = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):

        for w in range(W + 1):

            chamadas[0] += 1

            # caso base
            if i == 0 or w == 0:
                M[i][w] = 0

            # item cabe
            elif pesos[i] <= w:

                M[i][w] = max(
                    valores[i] + M[i - 1][w - pesos[i]],
                    M[i - 1][w]
                )

            # item não cabe
            else:
                M[i][w] = M[i - 1][w]

    return M[n][W]


# ─── Exemplo de uso ───────────────────────────────────────────────────────────

if __name__ == "__main__":

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

    pesos   = [0] + [item[0] for item in itens]
    valores = [0] + [item[1] for item in itens]

    chamadas = [0]

    inicio = time.perf_counter()

    resultado = mochila_pd(capacidade, pesos, valores, n, chamadas)

    fim = time.perf_counter()

    tempo = fim - inicio

    print("=== Problema da Mochila — Programação Dinâmica ===")
    print(f"Itens disponíveis : {itens}")
    print(f"Capacidade        : {capacidade}")
    print(f"Valor máximo      : {resultado}")
    print(f"Tempo de execução : {tempo:.15f} segundos")
    print(f"Número de chamadas: {chamadas[0]}")