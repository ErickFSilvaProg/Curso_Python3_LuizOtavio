"""
    — Listas em Python:
        https://docs.python.org/pt-br/3/tutorial/datastructures.html

        Tipo list - Mutável.
        
        Uma lista em Python é uma estrutura de dados mutável e ordenada usada para armazenar múltiplos itens em uma única variável.

        
        O que caracteriza uma lista em Python?
            
            • Uma coleção de itens entre colchetes [];
            • Os itens são separados por vírgulas;
            • Os dados podem variar entre diversos tipos de dados.

        
        Métodos úteis:

            → .append(value): Adiciona o argumento passado exatamente como um único item. Aumenta sempre em 1, independentemente do que você passar.
            
            → .extend(value): Percorre (itera) o objeto enviado e adiciona cada item individualmente na lista original. Aumenta de acordo com a quantidade de elementos que estavam dentro do iterável.
            
            → .insert(index, value): Adiciona um novo elemento em uma posição específica da lista, alterando a própria lista no local (in-place) e retornando "None".
            
            → .remove(value): Remove o primeiro valor encontrado na lista cujo valor é igual ao parâmetro informado e retorna "None".
           
            → .pop(index=-1): Remove o item na posição fornecida na lista e retorna o item removido. Se nenhum índice for especificado, remove e retorna o último item da lista.
            
            → .index(): Procura um elemento específico e retorna a posição (o número do índice) da primeira vez que esse elemento aparece. Pode-se limitar a busca definindo um ponto de início e de fim: lista.index(item, inicio, fim).
            
            → .count(value): Conta quantas vezes um valor específico aparece na lista e retorna esse número como um valor inteiro.
            
            → .sort(): Ordena os elementos de uma lista diretamente no local (in-place), alterando a própria lista original e retornando "None".
            
            → .reverse(): Inverte a ordem dos elementos na lista.
            
            → copy(): Devolve uma cópia rasa da lista.
            
            → del: Remove itens, fatias ou até a lista inteira usando o índice numérico da posição. (del lista[:])
            
            → clear(): Remove todos os itens de uma lista. Similar a del.
        
            
        — Erros conhecidos:

            Erro ao tentar acessar um índice que não existe na lista:
                ↪ IndexError: list index out of range
        
        — Tutorial sobre listas:
        (https://www.datacamp.com/pt/tutorial/python-list-methods)

"""

