"""
    — while/else em Python
    
        Quando o "break" é chamado dentro do while, o else não é executado.

"""


texto = 'Python-3.13'
i = 0

while i < len(texto):
    letra = texto[i]
    
    if letra == ' ':
        break
    
    print(letra)
    i += 1
else:
    print()
    print('O else foi executado...')

print()
print('Fora do while...')
print()