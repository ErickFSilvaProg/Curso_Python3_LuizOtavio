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


hexadecimal = 1024
print('O hexadecimal de {hexadecimal} é %04x' % (hexadecimal))