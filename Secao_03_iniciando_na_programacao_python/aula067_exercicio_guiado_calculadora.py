iniciar = input('Abrir calculadora? [S]im | [N]ão ').upper().startswith('S')
print()

if iniciar is False:
    print('Saiu do programa...')
    print()


while iniciar:
    
    numeros_validos = ...
    operadores_permitidos = '/*-+'
    
    
    # **********************************************
    # Entrada de dados:
    numero_1 = input('Digite o 1º número: ')
    operador = input('Digite o operador [/*-+]: ')
    numero_2 = input('Digite o segundo número: ')
    print()
    
    
    # **********************************************
    # Verificando as informações inseridas:
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
        
    except:
        numeros_validos = False
        
        
    if numeros_validos is False:
        print('Número inválido digitado.')
        print()
        continue
        
    if len(operador) > 1:
        print('Digite apenas um operador.')
        print()
        continue
        
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        print()
        continue
    
    
    # **********************************************
    # Processamento e resultado:
    try:
        
        if operador == '/':
            print(f'Resultado: {numero_1 / numero_2}')
        elif operador == '*':
            print(f'Resultado: {numero_1 * numero_2}')
        elif operador == '-':
            print(f'Resultado: {numero_1 - numero_2}')
        elif operador == '+':
            print(f'Resultado: {numero_1 + numero_2}')
        
        print()
        break
    
    except Exception as error:
        print(f'Erro encontrado: {error}')
        print()
