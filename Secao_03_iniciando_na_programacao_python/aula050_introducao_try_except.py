"""
    — Introdução ao try/except:
    
        try    -> Tenta executar o código neste bloco.
        except -> Caso ocorra algum erro na execução do código, este bloco será executado.
        
    
    O método .isdigit() em Python verifica se uma string é composta exclusivamente por caracteres numéricos, retornando True se isso for verdade e False caso contrário.

"""


# **************************************************************
number = input('Vou dobrar o número que você digitar: ')

if number.isdigit():
    number = float(number)

    print(
        f'O dobro de {number} é {number * 2:.1f}'
    )
else:
    print('Isso não é o número.')

print()


# **************************************************************
another_number = input('Vou triplicar o número digitado: ')

try:
    another_number = float(another_number)
    doubled_number = another_number * 2
    
    print(
        f'O dobro de {another_number} é {doubled_number:.1f}'
    )
except:
    print(
        'Isso não é um número'
    )

print()