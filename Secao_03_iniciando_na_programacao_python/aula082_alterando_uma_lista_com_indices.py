"""
    — Listas em Python:
        https://docs.python.org/pt-br/3/tutorial/datastructures.html

        Tipo list - Mutável.
        
        Uma lista em Python é uma estrutura de dados mutável e ordenada usada para armazenar múltiplos itens em uma única variável.

        
        O que caracteriza uma lista em Python?
            
            • Uma coleção de itens entre colchetes [];
            • Os itens são separados por vírgulas;
            • Os dados podem variar entre diversos tipos de dados.

        
        — Métodos úteis:

            • .append(value): Adiciona o argumento passado exatamente como um único item.
            Aumenta sempre em 1, independentemente do que você passar.
            
            • .extend(value): Percorre (itera) o objeto enviado e adiciona cada item individualmente na lista original.
            Aumenta de acordo com a quantidade de elementos que estavam dentro do iterável.
            
            • .insert(index, value): Adiciona um novo elemento em uma posição específica da lista, alterando a própria lista no local (in-place) e retornando "None".
            
            • .remove(value): Remove o primeiro valor encontrado na lista cujo valor é igual ao parâmetro informado e retorna "None".
           
            • .pop(index=-1): Remove o item na posição fornecida na lista e retorna o item removido.
            Se nenhum índice for especificado, remove e retorna o último item da lista.
            
            • .index(): Procura um elemento específico e retorna a posição (o número do índice) da primeira vez que esse elemento aparece.
            Pode-se limitar a busca definindo um ponto de início e de fim: lista.index(item, inicio, fim).
            
            • .count(value): Conta quantas vezes um valor específico aparece na lista e retorna esse número como um valor inteiro.
            
            • .sort(): Ordena os elementos de uma lista diretamente no local (in-place), alterando a própria lista original e retornando "None".
            
            • .reverse(): Inverte a ordem dos elementos na lista.
            
            • .copy(): Cria uma cópia rasa (ou shallow copy) de uma lista.
            Ele gera uma nova lista na memória com os mesmos elementos da lista original, mas de forma independente no primeiro nível.
            
            • del: Remove itens, fatias (slices) ou a própria lista diretamente pela sua posição (índice), sem retornar nenhum valor.
            Se você usar del sem especificar um índice, ele apaga a variável da lista por completo do escopo de memória.

                ↪ Remove por índice: Você informa a posição exata do elemento que deseja apagar (ex: del lista[0]).
                ↪ Remove fatias (slices): É possível apagar vários elementos de uma vez usando intervalos (ex: del lista[1:3]).
            
            • .clear(): Remove todos os itens de uma lista em Python, deixando-a vazia.
        
            
        — Erros conhecidos:

            Erro ao tentar acessar um índice que não existe na lista:
                ↪ IndexError: list index out of range
        
        — Tutorial sobre listas:
        (https://www.datacamp.com/pt/tutorial/python-list-methods)

"""

# Método .append() - list:
numeros = [1,2,3,4]
print(numeros)

numeros.append([5,6])
print(f'append(): {numeros}')
print()


# Método .extend() - list:
numeros = [1,2,3,4]
print(numeros)

numeros.extend([5,6])
print(f'extend(): {numeros}')
print()


# Método .insert() - list:
carros = ['polo','onix','hb20']
print(carros)

carros.insert(1,'PULSE')
print(f'insert(): {carros}')
print()


# Método .remove() - list:
nomes = ['João','Paulo','Gustavo','Pedro','Antônio']
print(nomes)

nomes.remove('Pedro')
print(f'.remove(): {nomes}')
print()


# Método .pop() - list:
paises = ['Brasil','Argentina','Paraguai','Chile']
print(paises)
print(f'Dado removido: {paises.pop(1)}')
print()


# Método .index() - list:
frutas = ['maçã','banana','cereja']
print(frutas)

posicao = frutas.index('banana')
print(f'index(): {posicao}')
print()


# Método .count() - lista:
frase = ['Tudo', 'passa', 'tudo', 'muda', 'tudo', 'se', 'renova']
print(frase)

repeticao = frase.count('tudo')
print(f'A palavra "tudo" repete-se {repeticao} vezes')
print()


# Método .sort() - list:
estados = ['Pernambuco','Bahia','Sergipe','Minas Gerais','Alagoas','Ceará','São Paulo','Rio de Janeiro']
print(estados)

estados.sort()
print(estados)
print()


# Métodos .reverse() - list:
dezenas = [20,50,10,40,60,30]
print(dezenas)

dezenas.sort()
dezenas.reverse()
print(dezenas)
print()


# Método .copy() - list:
animaisSelvagens = ['Leão','Tigre','Onça']
print(animaisSelvagens)

outrosAnimais = animaisSelvagens.copy()
outrosAnimais.extend(['Gato','Cachorro','Canário'])
print(animaisSelvagens)
print(outrosAnimais)
print()


# Comando del - list:
livrosEspiritas = ['O livro dos espíritos','Nosso lar','50 anos depois','Legião','Tambores de ângola']
print(livrosEspiritas)

del livrosEspiritas[2]
print(livrosEspiritas)

del livrosEspiritas[1:2]
print(livrosEspiritas)

del livrosEspiritas
# print(livrosEspiritas): NameError: name 'livrosEspiritas' is not defined
print()


# Método .clear() - list:
tiposDePao = ['frances','criolo','baiano','bolachão','doce','bola']
print(tiposDePao)

tiposDePao.clear()
print(tiposDePao)
print()