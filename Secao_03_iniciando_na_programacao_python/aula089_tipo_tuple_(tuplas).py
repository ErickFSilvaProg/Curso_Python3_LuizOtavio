"""
    — Tipo tuples (tuplas):

        •● Uma tupla em Python é uma estrutura de dados usada para armazenar uma coleção ordenada de elementos, caracterizada principalmente por ser imutável (ou seja, não pode ser alterada após ser criada).

            • Coleção ordenada: Os itens mantêm uma ordem fixa e cada um possui uma posição numérica chamada índice (começando em zero).
            
            • Imutável: Você não pode adicionar, remover ou modificar elementos depois que a tupla é definida.
            
            • Delimitação: É criada colocando os elementos entre parênteses ( ), separados por vírgulas, embora os parênteses sejam opcionais em alguns casos.

"""

# Tupla:
listaNomes = ['Maria','Helena','Luiz']
print(type(listaNomes))
print(listaNomes)
print()


# Convertendo uma lista em tupla:
tuplaNomes = tuple(listaNomes)
print(type(tuplaNomes))
print(tuplaNomes)
print()