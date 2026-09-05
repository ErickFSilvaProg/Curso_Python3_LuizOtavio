"""
    Faça um programa que peça o primeiro nome do usuário.
    
    Se o nome tiver 4 letras ou menos escreva:
        "Seu nome é curto";
    
    Se tiver entre 5 e 6 letras, escreva:
        "Seu nome é normal";
    
    Se for maior que 6 escreva:
        "Seu nome é muito grande".

"""

nome = input('Informe seu primeiro nome: ')
tamanho_letra = len(nome)

if tamanho_letra > 1:

    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Informe mais de uma letra')
    
print()