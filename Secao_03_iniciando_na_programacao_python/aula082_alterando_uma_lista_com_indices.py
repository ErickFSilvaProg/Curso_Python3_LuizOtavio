"""
    — Listas em Python:
        https://docs.python.org/pt-br/3/tutorial/datastructures.html

        Tipo list - Mutável.
        
        Uma lista em Python é uma estrutura de dados mutável e ordenada usada para armazenar múltiplos itens em uma única variável

        
        O que é uma lista?
            
            • Uma coleção de itens entre colchetes [].
            • Os itens são separados por vírgulas.
            • Os dados podem ser de vários tipos mistos.

        
        Métodos úteis:

            → append(value): Adiciona um item ao fim da lista.
            → extend(iterable): Estende a lista, adicionando no fim todos os elementos do argumento iterável passado como parâmetro.
            → insert(index, value): Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção
            → remove(value): Remove o primeiro item encontrado na lista cujo valor é igual ao parâmetro informado.
            → pop(index=-1): Remove o item na posição fornecida na lista e retorna. Se nenhum índice for especificado, remove e retorna o último item da lista. 
            → index(value[, start[, stop]]): Retorna o índice de base zero da primeira ocorrência de value na lista.
            → count(value): Devolve o número de vezes em que value aparece na lista.
            → sort(): Ordena os itens na lista.
            → reverse(): Inverte a ordem dos elementos na lista.
            → copy(): Devolve uma cópia rasa da lista.
            → del:
            → clear(): Remove todos os itens de uma lista. Similar a del.

"""

lista_numeros = [10, 20, 30, 40]

print(lista_numeros)
print(lista_numeros[2])

lista_numeros[2] = 300
print(lista_numeros)

del lista_numeros[2]
print(lista_numeros)

lista_numeros.append(50)
print(lista_numeros)

item_removido = lista_numeros.pop()
print('Item removido: ', item_removido, type(item_removido))
print(lista_numeros)