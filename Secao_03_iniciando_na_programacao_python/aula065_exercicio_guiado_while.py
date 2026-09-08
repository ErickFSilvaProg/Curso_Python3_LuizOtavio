"""
    — Interagindo string com while

"""

#       01234567890123
nome = 'Erick Ferreira'
#      -43210987654321
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'|{letra}'
    indice += 1

print(novo_nome)
print()