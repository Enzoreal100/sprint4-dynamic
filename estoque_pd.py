# Constantes e variáveis de entrada do problema

T = 7  # Horizonte de planejamento (dias)
D = [10, 5, 20, 12, 8, 15, 6]  # Demanda diária prevista
C_order = 50  # Custo fixo por pedido
C_hold = 1  # Custo de manutenção por item por dia

def custo_manutencao(t, k, D, C_hold):
    """Calcula o custo de manutenção para um pedido feito no dia t que cobre a demanda até o dia k."""
    custo = 0
    for i in range(t + 1, k + 1):
        custo += D[i] * (i - t) * C_hold
    return custo


def resolver_top_down(t, T, D, C_order, C_hold, memo):
    """
    Resolve o problema de otimização de estoque usando a abordagem Top-Down (recursiva com memorização).
    """
    if t >= T:
        return 0

    if memo[t] != -1:
        return memo[t]

    custo_minimo = float('inf')

    for k in range(t, T):
        custo_manutencao_atual = custo_manutencao(t, k, D, C_hold)

        custo_futuro = resolver_top_down(k + 1, T, D, C_order, C_hold, memo)

        custo_total = C_order + custo_manutencao_atual + custo_futuro

        if custo_total < custo_minimo:
            custo_minimo = custo_total

    memo[t] = custo_minimo

    return custo_minimo


def iniciar_top_down(T, D, C_order, C_hold):
    """Inicializa a memorização e chama a função top-down."""
    memo = [-1] * T
    return resolver_top_down(0, T, D, C_order, C_hold, memo)


def resolver_bottom_up(T, D, C_order, C_hold):
    """Resolve o problema de otimização de estoque usando a abordagem Bottom-Up (iterativa)."""
    dp = [0] * (T + 1)

    for t in range(T - 1, -1, -1):
        custo_minimo_t = float('inf')
        for k in range(t, T):
            custo_manutencao_atual = custo_manutencao(t, k, D, C_hold)
            custo_total = C_order + custo_manutencao_atual + dp[k + 1]
            if custo_total < custo_minimo_t:
                custo_minimo_t = custo_total
        dp[t] = custo_minimo_t

    return dp[0]



