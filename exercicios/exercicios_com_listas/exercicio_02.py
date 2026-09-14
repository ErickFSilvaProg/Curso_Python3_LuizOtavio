"""
Dashboard de Vendas (Análise de Dados): você recebeu uma lista com as vendas diárias de uma equipe:

vendas = [1500, 2000, 800, 3500, 1200].

Crie um programa que exiba um pequeno relatório contendo:

1. O total de vendas na semana.
2. A média de vendas diária.
3. O valor da melhor venda e da pior venda do período.

"""

# Lista:
lista_vendas = [1500, 2000, 800, 3500, 1200]


# 1. O total de vendas na semana.
total_vendas = 0

for valor in lista_vendas:
    total_vendas += valor

print(f'Total de vendas: {total_vendas}')


# 2. A média de vendas diária.
media_diaria = 0
total_vendas2 = 0

for valor in lista_vendas:
    total_vendas2 += valor
    media_diaria = total_vendas2 / len(lista_vendas)

print(f'Média de vendas diária: {media_diaria:.2f}')


# O valor da melhor venda e da pior venda do período.
melhor_venda = max(lista_vendas)
pior_venda = min(lista_vendas)

print(f'Maior venda: {melhor_venda}')
print(f'Menor venda: {pior_venda}')