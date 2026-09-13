"""
    — Listas em Python:
        https://docs.python.org/pt-br/3/tutorial/datastructures.html

        Tipo list - Mutável.
        
        Uma lista em Python é uma estrutura de dados mutável e ordenada usada para armazenar múltiplos itens em uma única variável

        
        O que é uma lista?
            
            • Uma coleção de itens entre colchetes [].
            • Os itens são separados por vírgulas.
            • Os dados podem ser de vários tipos mistos.

"""

# String:
texto = 'Python'
print(len(texto))
print()


# List:
nomes = list()
print(type(nomes))

nomes2 = []
print(type(nomes2))
print()


lista = [123, True, 'Erick Ferreira', 7564.45, []]
print(lista)
print(lista[2].upper())

lista[2] = 'Erick'
print(lista)