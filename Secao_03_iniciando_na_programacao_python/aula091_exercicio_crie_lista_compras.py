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


# Programa:
while True:

    try:

        print()
        print('📄 Lista de compras...')
        opcao = input('[i]nserir | [l]istar | [a]pagar: ').lower()

        if opcao != 'i' and opcao != 'l' and opcao != 'a':
            
            # Forçando um erro do tipo ValueError caso as opções sejam outras. 
            raise ValueError('Opção inválida...')
        
        if opcao == 'i':

            os.system("cls" if os.name == "nt" else "clear")

            addItem = ...
            print()
            print('📄 Lista de compras...')
            while addItem != '':
                addItem = input('Nome do produto: ')

                if addItem != '':
                    lista_produtos.append(addItem)

        if opcao == 'l':

            os.system("cls" if os.name == "nt" else "clear")

            # print()
            for indice, item in enumerate(lista_produtos, start=1):
                print(f'{indice}. {item}')

        if opcao == 'a':

            os.system("cls" if os.name == "nt" else "clear")

            for indice, item in enumerate(lista_produtos, start=1):
                print(f'{indice}. {item}')
            
            remItem = ...
            print()
            print('📄 Lista de compras...')
            remItem = input('Item a ser removido: ')
            lista_produtos.remove(remItem)

    except ValueError as e:

        os.system("cls" if os.name == "nt" else "clear")
        
        print(f'{e}')
        continue

    # break