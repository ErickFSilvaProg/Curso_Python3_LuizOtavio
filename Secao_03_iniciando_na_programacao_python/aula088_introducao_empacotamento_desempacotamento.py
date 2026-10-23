"""
    — Introdução ao empacotamento e desempacotamento:

        •● Empacotamento e desempacotamento, em Python, são mecanismos que permitem agrupar múltiplos valores em uma única estrutura de dados ou espalhar os elementos de uma coleção em variáveis e argumentos individuais.

            
            • Empacotamento (Packing): O empacotamento acontece quando você junta vários valores soltos e os coloca dentro de uma única estrutura, geralmente uma tupla.
            
            Quando você separa valores por vírgulas sem colchetes ou chaves, o Python cria uma tupla automaticamente.

                ↪ Empacotando valores em uma tupla chamada "dados":
                    
                    dados = "Ana", 25, "Engenheira"
                    print(dados)  # Saída: ('Ana', 25, 'Engenheira')
                
            Em funções (*args e **kwargs): O empacotamento também é usado para aceitar um número variável de argumentos em uma função usando o asterisco (* para posicionais e ** para nomeados)

            • Desempacotamento (Unpacking): O desempacotamento faz o oposto, ele pega uma coleção (como uma lista, tupla ou dicionário) e distribui cada um dos seus elementos em variáveis separadas.
            
            O número de variáveis do lado esquerdo deve ser exatamente igual ao número de elementos da coleção do lado direito.

                ↪ Dempacotando valores de uma tupla chamada "coordenada":

                    coordenada = (10, 20)
                    x, y = coordenada

                    print(x)  # Saída: 10
                    print(y)  # Saída: 20

            • Uso do operador asterisco (*): O asterisco permite o desempacotamento parcial ou a captura de múltiplos argumentos.

                ↪ Em atribuições: O * captura o restante dos itens em formato de lista:

                    primeiro, *resto = [10, 20, 30, 40]
                    print(primeiro)  # Saída: 10
                    print(resto)     # Saída: [20, 30, 40]
                
                ↪ Em funções: Permite passar uma lista inteira como argumentos separados.

"""

# Empacotamento:
lista = 'Python', 3.15, 2026
print(type(lista))
print(lista)
print()


# Desempacotamento:
dado1, dado2, dado3 = lista

print(dado1)
print(dado2)
print(dado3)
print()

dado1, *_ = lista
print(dado1)

for dado in _:
    print(dado)

print()