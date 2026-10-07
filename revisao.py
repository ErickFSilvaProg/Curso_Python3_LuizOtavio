palavraSecreta = 'Brasil'
letraDigitada = ''
letrasDaPalavra = ''


print('PALAVRA SECRETA...')

while letrasDaPalavra != palavraSecreta:
    letraDigitada = input('Digite uma letra: ')

    if letraDigitada in palavraSecreta:
        letrasDaPalavra += letraDigitada

print(letraDigitada)