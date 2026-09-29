"""
    — Imprecisão dos números de ponto flutuante:

        Double-precision
        Floating-point
        Format IEEE 754

"""

import decimal

num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2

num_4 = decimal.Decimal(0.1)
num_5 = decimal.Decimal(0.7)
num_6 = num_4 + num_5


print(num_3)
print(f'{num_3:.1f}')
print(round(num_3, 1))
print()

print(decimal.Decimal(num_3))
print(decimal.Decimal(num_6))
print(num_6)
print()