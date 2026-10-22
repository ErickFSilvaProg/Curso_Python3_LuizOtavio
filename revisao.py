# Método .append() - list:
numeros = [1,2,3,4]
print(numeros)
numeros.append([5,6])
print(f'append(): {numeros}')
print()


#Método .extend() - list:
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
dezenas.reverse()
print(dezenas)
print()


# Exemplo final:
pessoas = [
    [1,'Erick Ferreira','Programador python',6756.87],
    [2,'Gabriel Ferreira','Engenheiro civil',8829.92]
]

for pessoa in pessoas:
    
    for info in pessoa:
        print(info)
    
    print()