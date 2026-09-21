"""
    — Enumerate — Enumera iteráveis (índices)

        A função enumerate() em Python serve para adicionar um contador a um iterável (como uma lista ou tupla), permitindo que você obtenha o índice e o valor de cada item ao mesmo tempo durante um loop for.

        Sem usar o enumerate, você precisaria criar uma variável de contagem manual ou usar range(len()). Com ela, o código fica mais limpo e direto.
        Por padrão, a contagem começa no número 0. Você pode mudar isso usando o parâmetro opcional start:

            frutas = ["maçã", "banana", "uva"]
            for indice, fruta in enumerate(frutas, start=1):
                print(f"{indice}: {fruta}")

"""

lista_nomes = ['Maria','Helena','Luiz']
lista_nomes.append('João')

# Com o enumerate:
for indice, nome in enumerate(lista_nomes, start=1):
    print(f'{indice}. {nome}')
print()

# Sem o enumerate:
for nome in lista_nomes:
    print(nome)
print()