"""
    Coerção de tipos em Python (Conversão de tipos):

        Type convertion, typecasting ou coercion é o ato de converter um tipo em outro tipo imutável e primitivo.

            ↪ Tipos primitivos: str, int, float, bool.
        
            
        O Python é uma liguagem de tipagem dinâmica e forte.

            ↪ Forte porque ele não converterá um tipo em outro de forma automática.
        
        Para haver uma coerção de tipos no Python ela precisará ser explícita.
        
        Uma string vazia é considerada "False".
        Uma string com alguma coisa é considerada "True".

"""

print(1 + 1)
print('a' + 'b')
print()

# TypeError: can only concatenate str (not "int") to str.
# print('1' + 1)
# print()


# Coerção str para int:
print(int('1'), type(int('1')))
print()


# Coerção str para float:
print(float('1.1'), type(float('1.1')))
print()


# Coerção str para bool:
print(bool(''), type(bool('')))
print(bool(' '), type(bool(' ')))
print()


# Coerção de int para str:
print(str(11) + 'b', type(str(11) + 'b'))
print()