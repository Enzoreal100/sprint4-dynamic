# Projeto de Otimização de Estoque com PD

## Contextualização do Problema

O gerenciamento de estoque é um desafio crítico para muitas empresas. Um controle ineficiente pode levar a dois problemas principais: excesso de estoque, que gera altos custos de manutenção, e falta de estoque, que resulta em perda de vendas e clientes insfeitos. Este projeto aborda esse desafio através de uma solução de otimização.

O problema é modelado como um problema de Lot-Sizing determinístico. Isso significa que a demanda para um determinado período de tempo é conhecida com antecedência. O objetivo é determinar quando e quanto pedir de um determinado produto para minimizar o custo total, que é uma combinação do custo fixo de fazer um pedido e o custo de manter os itens em estoque.

## Estruturas de Dados e Algoritmos

Para resolver este problema, utilizamos Programação Dinâmica (PD), uma técnica poderosa para resolver problemas de otimização que podem ser divididos em subproblemas sobrepostos.

- **`D[]` (Array de Demanda):** Este array é a entrada fundamental do problema. `D[i]` armazena a demanda para o dia `i`. É com base nesses valores que todos os custos são calculados.

- **`memo[]` e `dp[]` (Arrays de Memorização):** Ambos os arrays são usados para armazenar as soluções de subproblemas já resolvidos, evitando recálculos desnecessários. `memo[]` é usado na abordagem Top-Down (recursiva) e `dp[]` na abordagem Bottom-Up (iterativa). `dp[t]` ou `memo[t]` armazena o custo mínimo para satisfazer a demanda do dia `t` até o final do horizonte de planejamento.

### Abordagem Top-Down (Recursiva com Memorização)

A função `resolver_top_down` quebra o problema original em subproblemas menores de forma recursiva. Ela começa do dia `t=0` e explora as decisões possíveis. Para cada dia `t`, a função decide atender a demanda até um dia `k` (com `k >= t`). O custo dessa decisão é o custo de fazer um pedido hoje, mais o custo de manter o estoque para os dias `t+1` até `k`, mais o custo ótimo para o resto do período (que é resolvido pela chamada recursiva `resolver_top_down(k + 1, ...)`). A memorização garante que, uma vez que o custo ótimo para um dia `t` é calculado, ele é armazenado e reutilizado.

### Abordagem Bottom-Up (Iterativa)

A função `resolver_bottom_up` resolve o problema de forma iterativa, começando pelos menores subproblemas. Ela calcula o custo ótimo do último dia para trás até o primeiro. O array `dp` é preenchido de `T-1` até `0`. Para cada dia `t`, ela calcula o custo de todas as decisões possíveis (fazer um pedido que cubra a demanda até o dia `k`) e escolhe a que minimiza o custo total. Como ela itera de trás para frente, o custo ótimo para os subproblemas futuros (`dp[k+1]`) já está disponível quando necessário.

### Exploração do Espaço de Decisão

Ambas as abordagens utilizam loops aninhados (ou uma estrutura recursiva equivalente) para explorar o espaço de decisões. O loop externo itera sobre o dia `t` para o qual estamos tomando uma decisão. O loop interno itera sobre o dia `k`, que representa até quando um pedido feito no dia `t` irá cobrir a demanda. Essa estrutura garante que todas as combinações de "quando pedir" e "quanto pedir" (indiretamente, ao decidir até quando o pedido cobre) sejam avaliadas para encontrar a solução de custo mínimo.

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
