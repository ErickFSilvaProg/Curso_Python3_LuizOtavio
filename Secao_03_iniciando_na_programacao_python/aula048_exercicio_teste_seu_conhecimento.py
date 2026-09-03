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

# PROGRAM...

# Variables:
name = input('What\'s your name? ')
age = input('What\'s your age? ')
print()


if name and age:

    name_reversed = name[::-1]
    name_space = ...
    numbers_of_letter = len(name)
    first_letter = name[0]
    last_letter = name[-1]


    if ' ' in name:
        name_space = 'contém'
    else:
        name_space = 'não comtém'


    print(f'Your name is {name}')
    print(f'Your name reversed is {name_reversed}')
    print(f'Your name contains (or does not contains) {name_space} space(s)')
    print(f'Your name has {numbers_of_letter} letter(s)')
    print(f'The first letter of your name is {first_letter}')
    print(f'The last letter of your name is {last_letter}')
else:
    print('Sorry, you left fields blank!')

print()