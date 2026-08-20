"""
    input() é uma funçaõ que solicita dados ao usuário.
    Tudo o que for coletado por essa função será do tipo string.
    Se for preciso realizar algum cálculo, será necessário a coerção de tipos.

"""

# Entrada de dados:
numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

# Typecast:
int_numero1 = int(numero1)
int_numero2 = int(numero2)

# Saída de dados:
print(f'A soma dos dois números é: {int_numero1 + int_numero2}')