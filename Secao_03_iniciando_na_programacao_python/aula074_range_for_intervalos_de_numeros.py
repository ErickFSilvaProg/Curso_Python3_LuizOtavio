"""
    — Em Python, a função range() serve para gerar uma sequência imutável de números inteiros em um intervalo determinado.
    
        A função aceita até três argumentos: 
        
            range(inicio, fim, passo).
        
            • Início (start): Onde a sequência começa (o padrão é 0).
            • Fim (stop): O limite da sequência, que não é incluído no resultado (obrigatório).
            • Passo (step): O incremento ou salto entre os números (o padrão é 1)
        
        Ao informar apenas um valor no range, este será o valor do "stop".

"""

nome = 'Erick'
# Os últimos números dos ranges não serão impressos:
numeros_1 = range(10)
numeros_2 = range(3,len(nome))
numeros_3 = range(2,-10,-2)


for i in numeros_1:
    print(i)
print()

for i in numeros_2:
    print(i)
print()

for i in numeros_3:
    print(i)
print()