"""
    Ordem de execução dos operadores aritméticos:

        1. (parênteses)
        
        2. **
        
        3. * / // %
            ↪ Se houver mais de um na mesma linha, o Python resolve da esquerda para a direita.
        
        4. + -
            ↪ Se houver mais de um na mesma linha, o Python resolve da esquerda para a direita.

"""

conta1 = 1 + 1 ** 5 + 5
print(conta1)


conta2 = (1 + 1) ** 5 + 5
print(conta2)


conta3 = 1 + 1 ** (5 + 5)
print(conta3)


conta4 = (1 + 1) ** (5 + 5)
print(conta4)