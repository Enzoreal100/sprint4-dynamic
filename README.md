# Projeto de Otimização de Estoque com PD

## Contextualização do Problema

O gerenciamento de estoque é um desafio crítico para muitas empresas. Um controle ineficiente pode levar a dois problemas principais: excesso de estoque, que gera altos custos de manutenção, e falta de estoque, que resulta em perda de vendas e clientes insfeitos. Este projeto aborda esse desafio através de uma solução de otimização.

O problema é modelado como um problema de Lot-Sizing determinístico. Isso significa que a demanda para um determinado período de tempo é conhecida com antecedência. O objetivo é determinar quando e quanto pedir de um determinado produto para minimizar o custo total, que é uma combinação do custo fixo de fazer um pedido e o custo de manter os itens em estoque.

## Estruturas de Dados e Algoritmos

Para resolver este problema, utilizamos Programação Dinâmica (PD), uma técnica poderosa para resolver problemas de otimização que podem ser divididos em subproblemas sobrepostos.

### Estruturas de Dados Utilizadas

- **`D[]` (Array de Demanda):** Este array é a entrada fundamental do problema. `D[i]` armazena a demanda para o dia `i`. É com base nesses valores que todos os custos são calculados. No contexto do estoque, representa quantos itens são necessários em cada período, permitindo calcular o custo de manutenção quando decidimos comprar antecipadamente.

- **`memo[]` e `dp[]` (Arrays de Memorização):** Ambos os arrays são usados para armazenar as soluções de subproblemas já resolvidos, evitando recálculos desnecessários. `memo[]` é usado na abordagem Top-Down (recursiva) e `dp[]` na abordagem Bottom-Up (iterativa). `dp[t]` ou `memo[t]` armazena o custo mínimo para satisfazer a demanda do dia `t` até o final do horizonte de planejamento. Isso é crucial para o problema de estoque pois evita recalcular cenários de compra já analisados.

### Aplicação da Programação Dinâmica

**Subproblema:** Para cada dia `t`, qual o custo mínimo para atender toda a demanda de `t` até o final do período?

**Decisão:** Em cada dia `t`, decidir fazer um pedido que cubra a demanda até o dia `k` (onde `k ≥ t`).

**Função de Recorrência:** 
`custo_minimo(t) = min{custo_pedido + custo_manutencao(t,k) + custo_minimo(k+1)}` para todos os `k` válidos.

**Caso Base:** `custo_minimo(T) = 0` (após o último dia, não há mais custos).

### Abordagem Top-Down (Recursiva com Memorização)

A função `resolver_top_down` quebra o problema original em subproblemas menores de forma recursiva. Ela começa do dia `t=0` e explora as decisões possíveis. 

**Como funciona no contexto do estoque:**
- Para cada dia `t`, a função decide fazer um pedido que atenda a demanda até o dia `k` (com `k ≥ t`)
- O custo dessa decisão inclui: custo fixo do pedido + custo de manter estoque dos dias `t+1` até `k` + custo ótimo do restante do período
- A memorização evita recalcular o mesmo subproblema, crucial quando há muitas opções de compra sobrepostas
- **Vantagem:** Intuitiva, resolve apenas os subproblemas necessários
- **Complexidade:** O(T²) tempo e O(T) espaço

### Abordagem Bottom-Up (Iterativa)

A função `resolver_bottom_up` resolve o problema de forma iterativa, começando pelos menores subproblemas.

**Como funciona no contexto do estoque:**
- Calcula o custo ótimo do último dia para trás até o primeiro
- O array `dp` é preenchido de `T-1` até `0`, garantindo que soluções futuras estejam disponíveis
- Para cada dia `t`, avalia todas as estratégias de compra possíveis (cobrir demanda até diferentes dias `k`)
- Escolhe a estratégia que minimiza: custo do pedido + custo de manutenção + custo ótimo futuro
- **Vantagem:** Sem overhead de recursão, mais eficiente em memória
- **Complexidade:** O(T²) tempo e O(T) espaço

### Exploração do Espaço de Decisão

Ambas as abordagens utilizam loops aninhados (ou uma estrutura recursiva equivalente) para explorar o espaço de decisões de forma sistemática.

**Estrutura da Exploração:**
- **Loop externo (dia `t`):** Itera sobre cada dia do horizonte de planejamento onde uma decisão de compra pode ser tomada
- **Loop interno (dia `k`):** Para cada dia `t`, explora todas as opções de "até quando" o pedido feito em `t` deve cobrir a demanda

**Aplicação no Problema de Estoque:**
- Cada combinação `(t,k)` representa uma estratégia: "fazer pedido no dia `t` para cobrir demanda até o dia `k`"
- O algoritmo calcula o custo de cada estratégia: `custo_fixo + soma_manutencao(t+1, k) + custo_otimo_futuro(k+1)`
- A quantidade do pedido é determinada indiretamente pela soma das demandas de `t` até `k`
- Essa exploração garante que encontremos a combinação ótima de "quando comprar" e "quanto comprar"

**Complexidade do Espaço de Decisão:** O(T²) combinações possíveis, onde T é o número de dias no horizonte de planejamento.

## Como Compilar e Executar

O código foi escrito em Python e não requer compilação. Para executar os testes e ver os resultados, utilize o seguinte comando:

```bash
py teste_estoque.py
```

(Use `python` em vez de `py` se for o seu executável padrão).

A saída esperada é:

```
Custo mínimo (Top-Down): 189
Custo mínimo (Bottom-Up): 189

Os resultados das duas abordagens são iguais. Teste passou!
```
