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
opcaoMenu = ''


# Programa:
while True:

    try:

        # *****************************************************
        # MENU DO PROGRAMA:
        print()
        print('📄 Lista de compras...')
        opcaoMenu = input('[i]nserir | [l]istar | [a]pagar: ').lower()

        if opcaoMenu != 'i' and opcaoMenu != 'l' and opcaoMenu != 'a':
            
            # Forçando um erro do tipo ValueError caso as opções sejam outras. 
            raise ValueError('Opção inválida...')


        # *****************************************************
        # OPÇÃO PARA INSERIR DADOS NA LISTA:
        if opcaoMenu == 'i':

            os.system("cls" if os.name == "nt" else "clear")

            addItem = ...
            
            print()
            print('📄 Lista de compras...')
            while addItem != '':
                addItem = input('Nome do produto: ')

                if addItem != '':
                    lista_produtos.append(addItem)

                if addItem == '':
                    os.system("cls" if os.name == "nt" else "clear")


        # *****************************************************
        # OPÇÃO PARA LISTAR OS DADOS DA LISTA:
        if opcaoMenu == 'l':

            os.system("cls" if os.name == "nt" else "clear")

            # print()
            for indice, item in enumerate(lista_produtos, start=1):
                print(f'{indice}. {item}')


        # *****************************************************
        # OPÇÃO PARA APAGAR OS DADOS DA LISTA:
        if opcaoMenu == 'a':
            
            remItem = ...
            flagError = ''
            
            print()
            print('📄 Lista de compras...')
            while remItem != '':
                os.system("cls" if os.name == "nt" else "clear")
                
                for indice, item in enumerate(lista_produtos, start=1):
                    print(f'{indice}. {item}')

                print()
                if flagError != '':
                    print(flagError)
                    flagError = ''
                    print()
                
                remItem = input('Número do item a ser removido: ')

                if remItem != '':

                    try:
                        remItem = int(remItem)
                        lista_produtos.pop(remItem - 1)
                    except:
                        flagError ='Digite o número do item.'
                        continue
                        
                if remItem == '':
                    os.system("cls" if os.name == "nt" else "clear")


    # *****************************************************
    # TRATANDO ERRO NO MENU DO PROGRAMA:
    except ValueError as e:

        os.system("cls" if os.name == "nt" else "clear")
        
        print(f'{e}')
        continue
