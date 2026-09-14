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
            → del: Remove itens, fatias ou até a lista inteira usando o índice numérico da posição. (del lista[:])
            → clear(): Remove todos os itens de uma lista. Similar a del.
        
            
        😅 Erros conhecidos:

            Erro ao tentar acessar um índice que não existe na lista:
                ↪ IndexError: list index out of range
        
        
        O método copy() "copia" os dados de uma lista para outra sem referencia-los.
        Os dados são copiados para outro setor da memória.

"""

nome = 'Erick'
print(nome)

nome = 'João'
print(nome)


# Passando valores por referência:
# *****************************************
lista_a = ['Luiz', 'Maria']
print(lista_a)

lista_b = lista_a
print(lista_b)

lista_a.append('Qualquer coisa')

print('Lista A:', lista_a)
print('Lista B:', lista_b)


# Copiando dados e não referenciando-os:
# *****************************************
lista_c = lista_a.copy()
lista_a.pop()

print('Lista A:', lista_a)
print('Lista C:', lista_c)
