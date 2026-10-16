lista_pessoas = []

while True:

    nome_digitado = input('Informe um nome ou digite "sair": ')

    if nome_digitado == 'sair':
        break

    if nome_digitado == '':
        print('Você não digitou nada 😅\n')
        continue

    lista_pessoas.append(nome_digitado)

print()

if len(lista_pessoas) == 0:
    print('📃 Lista vazia...\n')
else:
    lista_pessoas.sort()
    print("📃 Lista de pessoas:\n")

    for i in range(len(lista_pessoas)):
        print(f'{lista_pessoas[i]}')

print()