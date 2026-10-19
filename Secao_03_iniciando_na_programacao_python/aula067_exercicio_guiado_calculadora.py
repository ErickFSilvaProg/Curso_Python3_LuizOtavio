# CALCULADORA
# ********************************************
# Bibliotecas:
import os


# ********************************************
# Variáveis globais:
abrirCalculadora = ...
opcaoInvalida = ...
txtOpcInvalida = '\nOpção inválida!'

numerosInvalidos = False
msgErro = ''
novoCalculo = False


# ********************************************
# Programa: Tela de login.
print('Abrir calculadora?')
abrirCalculadora = input('[S]im | [N]ão: ').upper()

if abrirCalculadora != 'S' and abrirCalculadora != 'N':
    os.system('cls')
    opcaoInvalida = True

    while opcaoInvalida:
        os.system('cls')
        print(txtOpcInvalida)

        print('\nAbrir calculadora?')
        abrirCalculadora = input('[S]im | [N]ão: ').upper()

        if abrirCalculadora != 'S' and abrirCalculadora != 'N':
            continue
        else:
            opcaoInvalida = False
    
if abrirCalculadora == 'N':
    os.system('cls')
    abrirCalculadora = False
    print('\nPrograma encerrado...\n')


# ********************************************
# Programa: Entrada de dados.
if abrirCalculadora == 'S':
    os.system('cls')

while abrirCalculadora:
    # ********************************************
    # Variáveis locais:
    operadoresPermitidos = '+-*/'


    # ********************************************
    # Entrada de dados:
    if msgErro != '':
        os.system('cls')
        print()
        print(msgErro)
        msgErro = ''
        print()

    print('Qual operação você deseja realizar?')
    operador = input('Escolha o operador (+ - * /): ')
    print()

    if len(operador) > 1:
        print()
        msgErro = 'Digite apenas um operador.'
        continue

    if operador not in operadoresPermitidos:
        msgErro = f'O operadaor "{operador}" não é válido.'
        continue

    try:

        priNumero = float(input('Digie o 1º número: '))
        segNumero = float(input('Digie o 2º número: '))
    
    except:

        msgErro = 'Número inválido digitado.'
        continue


    # **********************************************
    # Processamento e resultado:
    try:
        os.system('cls')
        print()

        if operador == '+':
            print(f'Resultado: {priNumero + segNumero}')
            
        if operador == '-':
            print(f'Resultado: {priNumero - segNumero}')
            
        if operador == '*':
            print(f'Resultado: {priNumero * segNumero}')
            
        if operador == '/':
            print(f'Resultado: {priNumero / segNumero}')
    
    except Exception as erro:

        msgErro = f'Erro encontrado: \n{erro}'
        continue


    # **********************************************
    # Novo Cálculo ou encerrar sistema:
    print()
    print('Realizar outro cálculo?')
    novoCalculo = input('[S]im | [N]ão: ').upper().startswith('S')

    if novoCalculo:
        os.system('cls')
        continue
    else:
        os.system('cls')
        print('\nPrograma encerrado...\n')
        break