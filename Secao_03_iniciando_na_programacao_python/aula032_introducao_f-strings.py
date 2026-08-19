"""
    f-strings: Formatação de strings

"""

nome = 'Erick'
altura = 1.75
peso = 82
imc = ... # Elipse


print(imc)
imc = peso / (altura * altura)
print(imc)
print()


print(f'{nome} tem {altura:.2f} de altura. Pesa {peso} quilos e seu imc é de {imc:.2f}.')
print()