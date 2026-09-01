"""
    ● Operadores lógicos:
    
        and (e) - Todas as condições precisam ser verdadeiras.
        or (ou) - Qualquer condiçao verdadeira será avaliada como verdadeira.
        not (não) - Negação lógica. Inverte o resultado.

        Se qualquer valor for considerado verdadeiro, a expressão inteira será avalizada verdadeira.

        São considerados Falsy: 0, 0.0, '', False
        Também existe um tipo "None" que é usado para representar um "não valor".
"""


entrada = input('[E]ntrar | [S]air: ')
senha_permitida = '123456'


if (entrada == 'E' or entrada == 'e'):
    senha_digitada = input('Senha: ') or 'Sem senha'

    if senha_digitada == senha_permitida:
        print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito:
print(False or True)
print(True or False)
print(False or False)
print(False or False or 'abc')