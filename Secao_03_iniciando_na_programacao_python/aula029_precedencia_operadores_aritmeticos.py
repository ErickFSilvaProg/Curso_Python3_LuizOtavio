"""
    Ordem de execução dos operadores aritméticos:

        1. (parênteses)
        2. **
        3. * / // %
        4. + -

"""

conta1 = 1 + 1 ** 5 + 5
print(conta1)


conta2 = (1 + 1) ** 5 + 5
print(conta2)


conta3 = 1 + 1 ** (5 + 5)
print(conta3)


conta4 = (1 + 1) ** (5 + 5)
print(conta4)