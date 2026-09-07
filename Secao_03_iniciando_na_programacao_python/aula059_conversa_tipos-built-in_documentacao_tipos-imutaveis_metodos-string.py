"""
    — Tipos built-in:
        São tipos que já são internos no Python.
        Não precisamos instalar tais tipos no Python.
    
        Imutáveis (built-in) vistos anteriormente:
            str, int, float, bool.
    
    
    ● Tipos Numéricos:
        
        int: Números inteiros, positivos ou negativos (ex: 42).
        float: Números de ponto flutuante ou decimais (ex: 3.14).
        complex: Números complexos com parte real e imaginária (ex: 1 + 2j).
        
    
    ● Tipo Textual:
    
        str: Sequências de caracteres ou strings para textos (ex: "Olá, mundo").
    
    
    ● Tipo Booleano
    
        bool: Valores lógicos que podem ser True (verdadeiro) ou False (falso).
    
    
    ● Tipos de Sequência:
    
        list: Coleções ordenadas e mutáveis de itens (ex: [1, 2, 3]).
        tuple: Coleções ordenadas e imutáveis de itens (ex: (1, 2, 3)).
        range: Sequências numéricas imutáveis, muito usadas em laços de repetição (ex: range(0, 10)).
    
    
    ● Tipos de Mapeamento:
    
        dict: Dicionários que armazenam pares de chave e valor (ex: {"nome": "Ana", "idade": 25}).
    
    
    ● Tipos de Conjunto:
    
        set: Coleções não ordenadas de itens únicos e mutáveis (ex: {1, 2, 3}).
        frozenset: Versão imutável de um set.
    
    
    ● Tipos Binários:
    
        bytes: Sequências imutáveis de bytes (ex: b"texto").
        bytearray: Versão mutável de bytes.
        memoryview: Objetos de visualização de memória para acessar dados internos de outros objetos binários sem copiá-los.
        
    
    ● Tipo Especial:
    
        NoneType: Representa a ausência de valor, cujo único valor é None.

"""


# *******************************************************************
# Valores imutáveis: Os valores não copiados para outras variáveis.
# Tais valores não podem ser alterados.
# A variável poderá ser redeclarada.

nome = "Erick Ferreira"
print(nome)

# TypeError: 'str' object does not support item assignment
# nome[3] = 'y'

nome = f'{nome[:2]}y{nome[3:]}'
print(nome)
print()


# Métodos para str:
texto = 'o rato roeu a roupa do Rei de Roma'
num_carac = len(texto)

print(f'{texto} tem {num_carac} caracteres.')
print(texto.capitalize())
print(texto.upper())
print(texto.lower())
print(texto.zfill(num_carac * 2))
print()