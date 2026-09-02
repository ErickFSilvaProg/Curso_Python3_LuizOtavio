"""
    ● Operadores lógicos:
    
        and (e) - Todas as condições precisam ser verdadeiras.
        or (ou) - Qualquer condição verdadeira será avaliada como verdadeira.
        not (não) - Negação lógica. Inverte a expressão.

        São considerados Falsy: 0, 0.0, '', False
        Também existe um tipo "None" que é usado para representar um "não valor".
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'


if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avalização de curito circuito:
print(True and True)
print(True and True and True)
print(True and False and True)
print(True and 0 and True)
