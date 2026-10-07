"""
    O "while" é utilizado quando não sabemos quantas iterações acontecerão.
    Já o "for" é utilizado quando temos um número finito nas iterações do bloco.

"""


aviso = 'Deus, Pátria e Família!'

for i in range(30):

    if i == 13:
        alerta = 'Petista removido!!!'
        print(alerta)
        continue

    if i == 22:
        print('22 é Bolsonaro!!!')
        print(f'{aviso}')
        print()
        break

    print(i)
else:
    print()
    print(f'For completo com sucesso!')
    print()
