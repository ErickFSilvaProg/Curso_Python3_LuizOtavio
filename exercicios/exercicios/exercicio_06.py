# PROGRAMA:
import os

continuar = True
erro = ''

while continuar:
    os.system('cls')
    
    if erro:
        print(f'{erro}')
        erro = ''
        print()
    
    multiplicando = input('Qual tabuada exibir: ')

    if multiplicando.isdigit():
        multiplicando = int(multiplicando)
        multiplicadores = range(1,11)

        print()
        for multiplicador in multiplicadores:
            print(f'{multiplicando} x {multiplicador} =',multiplicando * multiplicador)

        print()
        novaTabuada = input('Nova tabuada [S]im | [N]ão? ').upper()

        if novaTabuada != 'S':
            break

        print()
    else:
        erro = f'Isso não é um número: {multiplicando}'

os.system('cls')
print('fim da tabuada...')
print()