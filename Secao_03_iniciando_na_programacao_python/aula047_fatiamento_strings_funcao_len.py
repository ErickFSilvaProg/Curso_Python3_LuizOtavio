"""
    — Fatiamento de string e a função len:

        Strings em Python são iteráveis.

            012345678
            Olá mundo
           -987654321
    
        Fatiamento [i:f:p] [::]

            i -> início
            f -> fim
            p -> passo. Informa de quantos em quantos os caracteres serão pulados.

        Obs.: A função "len" retorna a quantidade de caracteres da str.

"""

#           012345678
saudacao = 'Olá mundo'
#          -987654321

final = len(saudacao)


# ************************************
# Recuperando valores na string por índices:
print(saudacao[5])
print(saudacao[-4])


# ************************************
# Recuperar valores na string por fatiamento:

## De uma posição até o fim da string:
print(saudacao[4:])
print(saudacao[-5:])

## De uma posição até outra posição: A última posição será omitida.
print(saudacao[0:3])

## Do início até uma determinada posição: Omitindo o início.
print(saudacao[:3])


# ************************************
# Função len: Utilizada para contar caracteres.
print(len(saudacao[3]))
print(len(saudacao))

# Utilizando o [p]: Passo.
print(saudacao[0:len(saudacao):2])

# Utilizando o [p] negativo: Inverterá o posição da leitura.
print(saudacao[::-1])