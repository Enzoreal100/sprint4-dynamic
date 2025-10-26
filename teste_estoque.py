from estoque_pd import iniciar_top_down, resolver_bottom_up

T = 7
D = [10, 5, 20, 12, 8, 15, 6]
C_order = 50
C_hold = 1

resultado_top_down = iniciar_top_down(T, D, C_order, C_hold)
print(f"Custo mínimo (Top-Down): {resultado_top_down}")

resultado_bottom_up = resolver_bottom_up(T, D, C_order, C_hold)
print(f"Custo mínimo (Bottom-Up): {resultado_bottom_up}")

assert resultado_top_down == resultado_bottom_up

print("\nOs resultados das duas abordagens são iguais. Teste passou!")
