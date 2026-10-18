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
msgErro = ...


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
    if numerosInvalidos:
        os.system('cls')
        print()
        print(msgErro)
        print()

    print('Qual operação você deseja realizar?')
    operador = input('Escolha o operador (+ - * /): ')
    print()

    priNumero = input('Digie o 1º número: ')
    segNumero = input('Digie o 2º número: ')


    # **********************************************
    # Verificando as informações inseridas:
    try:
        priNumero = float(priNumero)
        segNumero - float(segNumero)
    except:
        msgErro = 'Entrada inválida'
        numerosInvalidos = True
        continue

    if len(operador > 1):
        print()
        print('Digite apenas um operador.')
        continue

    if operador not in operadoresPermitidos:
        ...