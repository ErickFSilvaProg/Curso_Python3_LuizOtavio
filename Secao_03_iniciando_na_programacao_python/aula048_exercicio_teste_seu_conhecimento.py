"""
    — Exercício:

        1. Peça ao usuário para digitar seu nome
        2. Peça ao usuário para digitar sua idade
        3. Se o nome e a idade forem digitados:
            ↪ Exiba:

                a. Seu nome é {nome}
                b. Seu nome invertido é {nome_invertido}
                c. Seu nome contém (ou não) espaços
                d. Seu nome tem {n} letras
                e. A primeira letra do seu nome é {letra}
                f. A última letra do seu nome é {letra}
        
        4. Se nada for digitado em nome e em idade:
            ↪ Exiba:

                a. "Desculpe, você deixou campos vazios"

"""

# PROGRAMA

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

print()