"""
    Interpolação básica de strings:

        s     -> string
        d e i -> int
        f     -> float
        x e X -> Hexadecimal (1234567890ABCDEF)

"""

nome = 'Luiz'
preco = 100.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print()


decimal = 4538
print('O hexadecimal de %d é %04X' % (decimal, decimal))