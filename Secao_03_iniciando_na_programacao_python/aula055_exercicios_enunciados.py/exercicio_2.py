"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
    
        Ex.: Bom dia 0-11, 
             Boa tarde 12-17
             Boa noite 18-23.

"""

hora_atual = input('Informe a hora inteira: ')

if hora_atual.isdigit():
    hora_atual = int(hora_atual)

    if hora_atual >= 0 and hora_atual < 12:
        print('Bom dia! ☀️')
    elif hora_atual >= 12 and hora_atual < 18:
        print('Boa tarde! 🌅')
    elif hora_atual >= 18 and hora_atual <= 23:
        print('Boa noite" 🌛')
    else:
        print('Hora desconhecida!!!')
else:
    print(f'Hora em um formato diferente do solicitado.')

print()