# 🎒 Problema da Mochila (Knapsack Problem)

Implementações em Python do clássico **Problema da Mochila 0/1**, utilizando duas abordagens:
recursiva (força bruta) e programação dinâmica (bottom-up).

---

## 📋 Descrição do Problema

Dado um conjunto de `n` itens, cada um com um **peso** e um **valor**, e uma mochila com
**capacidade máxima W**, o objetivo é selecionar os itens que maximizem o valor total sem
exceder a capacidade.

Cada item só pode ser incluído **uma única vez** (versão 0/1).

---

## 📁 Arquivos

| Arquivo | Abordagem |
|---|---|
| `mochila_recursiva.py` | Recursão com divisão do problema em subproblemas |
| `mochila_dinamica.py` | Programação Dinâmica com tabela (bottom-up) |

---

## 🔁 Solução Recursiva — `mochila_recursiva.py`

### Funcionamento

A função `mochila(i, W, pesos, valores)` toma decisões item a item, de trás para frente:

1. **Caso base**: se não há mais itens (`i == 0`) ou a capacidade acabou (`W == 0`), retorna 0.
2. **Item não cabe**: se `pesos[i] > W`, o item é ignorado e avança-se para o anterior.
3. **Item cabe**: calcula recursivamente os dois cenários possíveis:
   - **Usar o item**: soma o valor do item ao melhor resultado com a capacidade reduzida.
   - **Não usar o item**: mantém a capacidade e passa para o item anterior.
4. Retorna o **máximo** entre as duas opções.

### Pseudocódigo

```
função mochila(i, W):
    se i == 0 ou W == 0:
        retorne 0
    se peso[i] > W:
        retorne mochila(i-1, W)
    usar     = valor[i] + mochila(i-1, W - peso[i])
    nao_usar = mochila(i-1, W)
    retorne max(usar, nao_usar)
```

### Complexidade

| Tipo | Complexidade |
|---|---|
| Tempo | O(2ⁿ) — exponencial |
| Espaço | O(n) — pilha de recursão |

> ⚠️ A solução recursiva recalcula os mesmos subproblemas várias vezes, tornando-se
> impraticável para entradas grandes.

### Como executar

```bash
python mochila_recursiva.py
```

### Exemplo de saída

```
=== Problema da Mochila — Solução Recursiva ===
Itens disponíveis : [(2, 6), (2, 10), (3, 12)]
Capacidade        : 5
Valor máximo      : 22
```

---

## 📊 Solução por Programação Dinâmica — `mochila_dinamica.py`

### Funcionamento

A função `mochila(n, W, pesos, valores)` preenche uma tabela `M[n+1][W+1]` de forma
iterativa (bottom-up):

1. **Inicialização**: toda a linha `i=0` e coluna `w=0` são preenchidas com 0 (casos base).
2. **Preenchimento**: para cada item `i` e cada capacidade `w`:
   - Se o item **não cabe** (`pesos[i] > w`): herda o resultado da linha anterior (`M[i-1][w]`).
   - Se o item **cabe**: escolhe o maior entre usar ou não usar o item.
3. A resposta final está em `M[n][W]`.

### Pseudocódigo

```
criar matriz M[n+1][W+1]
para i de 0 até n:
    para w de 0 até W:
        se i == 0 ou w == 0:
            M[i][w] = 0
        senão se peso[i] <= w:
            M[i][w] = max(
                valor[i] + M[i-1][w - peso[i]],
                M[i-1][w]
            )
        senão:
            M[i][w] = M[i-1][w]
```

### Complexidade

| Tipo | Complexidade |
|---|---|
| Tempo | O(n × W) — pseudo-polinomial |
| Espaço | O(n × W) — matriz completa |

> ✅ Cada subproblema é calculado **uma única vez** e armazenado na tabela,
> eliminando recálculos desnecessários.

### Como executar

```bash
python mochila_dinamica.py
```

### Exemplo de saída

```
=== Problema da Mochila — Programação Dinâmica ===
Itens disponíveis : [(2, 6), (2, 10), (3, 12)]
Capacidade        : 5

Matriz M[i][w]:
      w= 0   w= 1   w= 2   w= 3   w= 4   w= 5
-----------------------------------------------
i=0 |    0     0     0     0     0     0
i=1 |    0     0     6     6     6     6
i=2 |    0     0    10    10    16    16
i=3 |    0     0    10    12    16    22

Valor máximo      : 22
```

---

## ⚖️ Comparação entre as abordagens

| Critério | Recursiva | Programação Dinâmica |
|---|---|---|
| Tempo | O(2ⁿ) | O(n × W) |
| Espaço | O(n) | O(n × W) |
| Subproblemas repetidos | Sim | Não |
| Legibilidade | Alta | Média |
| Adequada para entradas grandes | ❌ | ✅ |

---

## 🔧 Estrutura das entradas

Ambas as implementações utilizam listas **1-indexadas** (o índice 0 é reservado como
sentinela para os casos base):

```python
# Exemplo com 3 itens
itens = [(2, 6), (2, 10), (3, 12)]  # (peso, valor)

pesos   = [0] + [item[0] for item in itens]  # [0, 2, 2, 3]
valores = [0] + [item[1] for item in itens]  # [0, 6, 10, 12]
capacidade = 5
```
