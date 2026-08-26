"""
    Exercício de programação com if e comparção.

"""

valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

valor1 = int(valor1)
valor2 = int(valor2)
print()


if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}')
elif valor2 > valor1:
    print(f'{valor2} é maior que {valor1}')
else:
    print(f'Os valores {valor1} e {valor2} são iguais!')