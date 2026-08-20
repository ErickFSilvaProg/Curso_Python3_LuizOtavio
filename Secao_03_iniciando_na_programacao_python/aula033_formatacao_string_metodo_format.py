"""
Tudo em Python é um objeto.
Objetos, geralmente, tem métodos dentro deles.
Os objetos contem ações que podem ser executadas, e essas ações são chamadas de métodos.
E métodos são funções que fazem alguma coisa com o objeto.
Os métodos recebem parâmetros e argumentos.
Após a nomeação de um parâmetro, todos os outros deveram ser nomeados.

"""

a = 'A'
b = 'B'
c = 1.1


# Sem parâmetros nomeados:
texto1 = 'a={} b={} c={:.2f}'
formato1 = texto1.format(a, b, c)
print(formato1)


# Recuperando os valores por índice e sem parâmetros nomeados:
texto2 = 'a={0} b={1} c={2}'
formato2 = texto2.format(a, b, c)
print(formato2)


# Recuperando os valores com parâmetros nomeados:
texto3 = 'a={nome1} b={nome2} c={nome3}'
formato3 = texto3.format(
    nome1=a, nome2=b, nome3=c
)
print(formato3)
