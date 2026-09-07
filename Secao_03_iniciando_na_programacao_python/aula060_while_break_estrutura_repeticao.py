"""
    — Repetições: while(enquanto)

        Executa uma ação enquanto uma condição for verdadeira.
    
    Atenção ao loop infinito!!!
    Utilize a palavra break no final do bloco while().

"""

condicao = True

while condicao:
    print(1)
    print(2)
    print(3)
    break
print()

while condicao:
    nome = input('Qual é seu nome: ')
    print(f'Seu nome é {nome}')
    break
print()

print('Acabou 🔚')
print()
