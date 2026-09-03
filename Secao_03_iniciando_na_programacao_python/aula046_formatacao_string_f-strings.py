"""
    — Formatação básica de strings:

        s      -> string
        d      -> int
        f      -> float
        .      -> <numero de dígitos>f
        x ou X -> Hexadecimal
        (caractere)(><^)(quantidade)
        >      -> Esquerda
        <      -> Direita
        ^      -> Centro
        Sinal  -> + ou -
        =      -> Força o sinal a aparecer antes dos zeros

            Ex.:0>-100,.1f
        
            
        Conversion flags:
        
            !r -> __repr__
            !s -> __str__
            !a -> __ascii__

"""

texto = 'Texto'
pi = 3.14159265359
numero = 4658
numero2 = -45398

print(f'{texto}')
print()


# Utilizando padding (preenchimento) na variável com texto:
print(f'{texto:•>11}')
print(f'{texto:•<11}')
print(f'{texto:•^11}')
print()


# Tratando casas decimais:
print(f'{pi:.1f}')


# Utilizando a vírgula para a separação de milhar:
print(f'{numero:,.2f}')
print()


# Utilizando operador aritmético para números positívos:
print(f'{numero:+.2f} (Positivo)')
print(f'{numero2:.2f} (Negatico não precisa do operador explícito)')
print()


# Utilizando padding (preenchimento) na variável com números:
print(f'{numero:0>+10,.2f}')
print(f'{numero:0=+10,.2f}')
print()


# Utilizando hexadecimal:
print(f'O hexadecimal de {numero} é {numero:08X}')
print()


# Utilizando conversion flags:
print(f'{texto!r}')
print(f'{texto!s}')
print(f'{texto!a}')
print()