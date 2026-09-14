# *************************************************
listaNomes = []
listaSair = ['SAIR','SAIr','SAir','Sair','sair',
             'sAir','saIr','saiR','',
             'sAIR','SaIR','SAiR','SAIr',
             'saIR','SAir','SaiR','sAIr'
            ]

while True:
    nome = input('Digite um nome: ')

    if nome in listaSair:
        break
    
    listaNomes.append(nome)

if listaNomes:
    print()
    for nome in listaNomes:
        print(nome)
print()


print('Fim do programa...')
print()