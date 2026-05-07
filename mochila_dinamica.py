# Problema da Mochila - Solução por Programação Dinâmica
# Complexidade de tempo: O(n * W)
# Complexidade de espaço: O(n * W)

def mochila(n, W, pesos, valores):
    """
    Resolve o Problema da Mochila usando Programação Dinâmica (bottom-up).

    Parâmetros:
        n (int): número de itens
        W (int): capacidade total da mochila
        pesos (list): lista de pesos dos itens (índice 1 até n)
        valores (list): lista de valores dos itens (índice 1 até n)

    Retorna:
        int: valor máximo que pode ser obtido
    """
    # Cria a matriz M[n+1][W+1] inicializada com 0
    M = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            # Caso base: sem itens ou sem capacidade
            if i == 0 or w == 0:
                M[i][w] = 0

            # O item i cabe — escolhe o melhor entre usar ou não usar
            elif pesos[i] <= w:
                usar     = valores[i] + M[i - 1][w - pesos[i]]
                nao_usar = M[i - 1][w]
                M[i][w]  = max(usar, nao_usar)

            # O item i não cabe — herda o resultado sem ele
            else:
                M[i][w] = M[i - 1][w]

    return M[n][W]


def imprimir_matriz(M, n, W):
    """Exibe a matriz de programação dinâmica de forma legível."""
    print("\nMatriz M[i][w]:")
    header = "     " + "  ".join(f"w={w:2d}" for w in range(W + 1))
    print(header)
    print("-" * len(header))
    for i in range(n + 1):
        linha = f"i={i} | " + "  ".join(f"{M[i][w]:4d}" for w in range(W + 1))
        print(linha)


# ─── Exemplo de uso ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Itens: (peso, valor)
    itens = [
        (2, 6),   # item 1
        (2, 10),  # item 2
        (3, 12),  # item 3
    ]

    n = len(itens)
    capacidade = 5

    # Listas 1-indexadas (índice 0 não é usado)
    pesos   = [0] + [item[0] for item in itens]
    valores = [0] + [item[1] for item in itens]

    # Reconstrói a matriz para exibição
    W = capacidade
    M = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                M[i][w] = 0
            elif pesos[i] <= w:
                M[i][w] = max(valores[i] + M[i - 1][w - pesos[i]], M[i - 1][w])
            else:
                M[i][w] = M[i - 1][w]

    resultado = M[n][W]

    print("=== Problema da Mochila — Programação Dinâmica ===")
    print(f"Itens disponíveis : {itens}")
    print(f"Capacidade        : {capacidade}")
    imprimir_matriz(M, n, W)
    print(f"\nValor máximo      : {resultado}")
