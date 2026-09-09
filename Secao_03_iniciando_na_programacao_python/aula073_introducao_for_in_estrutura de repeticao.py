"""
    — for / in:
    
        O comando "for" em Python serve para repetir um bloco de código para cada item de uma sequência ou coleção de dados.

"""

# 
texto  = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'|{letra}'

print(f'{novo_texto}|')
print()


# 
lista_carros = ['golf', 'gol', 'onix', 'tracker', 'mobi', 'pulse']

for carro in lista_carros:
    print(carro)

print()