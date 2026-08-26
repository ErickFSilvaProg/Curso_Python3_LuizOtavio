"""
    Operadores aritméticos: Hierarquia da Precedência.

        1. Parênteses: ( )
        
        2. Exponenciação: **
        
        3. Multiplicação, Divisão, Divisão Inteira e Módulo: *, /, //, %
            ↪ Se houver mais de um na mesma linha, o Python resolve da esquerda para a direita.
        
        4. Adição e Subtração: +, -
            ↪ Se houver mais de um na mesma linha, o Python resolve da esquerda para a direita.

"""

# Variáveis:
num2 = 2
num10 = 10
num25 = 25


# Parênteses:
print("Parênteses:", (num25 - num10) * num25)


# Exponenciação:
print('Exponenciação:', num2 ** num2)


# Multiplicação:
print('Multiplicação:', num25 * num10)


# Divisão:
print('Divisão:', num25 / num2)


# Divisão inteira: Sempre retornará um valor bool.
print('Divisão inteira:', num25 // num2)


# Módulo:
print('Módulo:', num25 % num2)


# Adição:
print('Adição:', num10 + num25)


# Subtração:
print('Subtração:', num10 - num25)


# Outros exemplos com "módulo" retornando "bool":
print()
print(num2 % num2 == 0)
print(num25 % num10 == 0)
print()

# ZeroDivisionError: integer modulo by zero
# print(num25 % 0 == 0)