import os

listaNomes = []
totalNomes = 0

qtdNomes = int(input('Quantos nomes quer armazenar? '))
print()

if totalNomes < qtdNomes:

    while totalNomes < qtdNomes:
        nomeDigitado = input('Digite um nome: ')
        # listaNomes.insert(totalNomes,nomeDigitado)
        listaNomes.append(nomeDigitado)
        totalNomes += 1

else:
    print('Você não quer armazenar nomes!')

if listaNomes != 0:
    os.system('cls')

    print('Nomes armazenados:\n')
    for i, nome in enumerate(listaNomes, start=1):
        print(f'{i}. {nome}')

print()