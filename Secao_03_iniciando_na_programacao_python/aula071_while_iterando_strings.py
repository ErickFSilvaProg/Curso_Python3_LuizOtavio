"""
    — O Python é uma linguagem case sensitive, o que significa que ele diferencia letras maiúsculas de minúsculas.
    
    — Método count():
    
        O método count() em Python serve para contar quantas vezes um elemento específico aparece dentro de uma estrutura de dados, como uma string, uma lista ou uma tupla.
        
            • Retorna um número inteiro com o total de ocorrências.
            • Não altera a estrutura original.
            • Retorna 0 se o elemento não for encontrado

"""



frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'

print(frase.count('Python'))
print(frase.count('python'))
print()
