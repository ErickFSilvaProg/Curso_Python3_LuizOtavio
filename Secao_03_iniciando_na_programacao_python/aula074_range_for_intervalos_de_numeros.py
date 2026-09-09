"""
    — Em Python, a função range() serve para gerar uma sequência imutável de números inteiros em um intervalo determinado.
    
        A função aceita até três argumentos: range(inicio, fim, passo).
        
            • Início (start): Onde a sequência começa (o padrão é 0).
            • Fim (stop): O limite da sequência, que não é incluído no resultado (obrigatório).
            • Passo (step): O incremento ou salto entre os números (o padrão é 1)
        
        Ao informar apenas um valor no range, este será o valor do "stop".

"""

numeros1 = range(1, 11)
numeros2 = range(1, 11, 2)
numeros3 = range(11)
numeros4 = range(-1, -11, -2)

for numero in numeros3:
    print(numero)