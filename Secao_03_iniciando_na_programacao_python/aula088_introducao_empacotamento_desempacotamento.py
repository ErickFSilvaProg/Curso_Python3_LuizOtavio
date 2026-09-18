"""
    — Introduçao ao empacotamento e desempacotamento:

        •● Empacotamento e desempacotamento em Python são recursos para agrupar múltiplos valores em uma única variável ou separar os elementos de uma coleção em variáveis individuais.

            • Empacotamento (Packing): O empacotamento acontece quando atribuímos vários valores separados por vírgula a uma única variável, criando automaticamente uma tupla. Também ocorre ao usar o asterisco (*) para juntar argumentos variáveis em funções.

                ↪ Empacotando valores em uma tupla:
                    dados = 1, 2, "Python"
                    print(dados)  # Saída: (1, 2, 'Python')

            
            • Desempacotamento (Unpacking): O desempacotamento ocorre quando pegamos os elementos de uma estrutura iterável (como uma lista ou tupla) e os distribuímos em várias variáveis separadas. Para isso funcionar perfeitamente, o número de variáveis deve corresponder à quantidade de itens.

                ↪ Desempacotando uma tupla:
                    a, b, c = (1, 2, "Python")
                    print(a)  # Saída: 1
                    print(b)  # Saída: 2
                    print(c)  # Saída: Python
            
            • Uso do operador Asterisco (*): O asterisco permite o desempacotamento parcial ou a captura de múltiplos argumentos.

                ↪ Em atribuições: O * captura o restante dos itens em formato de lista:

                    primeiro, *resto = [10, 20, 30, 40]
                    print(primeiro)  # Saída: 10
                    print(resto)     # Saída: [20, 30, 40]
                
                ↪ Em funções: Permite passar uma lista inteira como argumentos separados.

"""

listaNomes = ['Maria','Helena','Luiz']
print(listaNomes)
print()

nome1, nome2, nome3 = listaNomes
print(nome1)
print(nome2)
print(nome3)
print()

nome4, *_ = listaNomes
print(nome4)
print(_)
print()

for nome in _:
    print(nome)
print()