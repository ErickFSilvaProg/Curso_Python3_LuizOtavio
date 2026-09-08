"""
    — Calculadora com while

"""

while True:
    
    # *******************************
    # Entrada de dados:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o operador (/*-+): ')
    numero_2 = input('Digite outro número: ')
    numeros_validos = None
    
    
    # *******************************
    # Verificando as informações inseridas:
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
        print()
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos dos números digitados são inválidos.')
        print()
        continue
    
    operadores_permitidos = '/*-+'
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        print()
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        print()
        continue
    
    
    # *******************************
    # Processando as informações:
    if operador == '/':
        print(f'Resultado: {numero_1 / numero_2}')
    elif operador == '*':
        print(f'Resultado: {numero_1 * numero_2}')
    elif operador == '-':
        print(f'Resultado: {numero_1 - numero_2}')
    elif operador == '+':
        print(f'Resultado: {numero_1 + numero_2}')
    else:
        print('Nunca deveria chegar aqui!')
    print()
    
    
    # *******************************
    # Regra para sair da calculadora:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print()
    
    if sair:
        break