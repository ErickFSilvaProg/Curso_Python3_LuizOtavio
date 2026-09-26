"""
    — Exercício: Lista de compras.

        Faça uma lista de compras com "listas":
        
            O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
            Não permita que o programa quebre com erros de índices inexistentes na lista.

"""

# Bibliotecas:
import os


# Variáveis, listas:
lista_produtos = []
opcao = ''

# Limpa a tela dependendo do sistema operacional
# os.system("cls" if os.name == "nt" else "clear")

# Programa:
while True:

    try:
        print('📄 Lista de compras...')
        opcao = input('[i]nserir | [l]istar | [a]pagar: ')

        if opcao != 'i' and opcao != 'l' and opcao != 'a':
            # Forçando um erro do tipo ValueError caso as opções sejam outras. 
            raise ValueError('Opção inválida...')
        
        if opcao == 'i':
            print(f'\nOpção escolhida: {opcao}\n')

        if opcao == 'l':
            print(f'\nOpção escolhida: {opcao}\n')

        if opcao == 'a':
            print(f'\nOpção escolhida: {opcao}\n')

        # continue
    except ValueError as e:
        print(f'\n{e}\n')
        continue

    # break