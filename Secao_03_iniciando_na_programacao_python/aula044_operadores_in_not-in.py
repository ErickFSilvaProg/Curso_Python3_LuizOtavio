"""
    Operadores in e not in.

        in -> em (esté em)
        not in -> não em (não está em)
    
    
    Strings são iteráveis: Permite a navegação item por item.

        012345 (indices positivos)
        Otávio
       -654321 (indices negativos)

"""

nome = 'Otávio'

print(nome[2])
print(nome[-4])
print()

print('vio' in nome)
print('z' in nome)
print()

print('vio' not in nome)
print('zero' not in nome)
print()


nome = input("Digite seu nome: ")
encontrar = input('Encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

print()