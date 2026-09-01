"""
    Em Python, uma variável é um espaço na memória do computador usado para guardar dados.

    Você cria uma variável ao digitar o nome dela seguido do sinal de igual (=) para dar um valor a mesma. Não precisando declarar o tipo antes.

    Regras da PEP8: https://peps.python.org/pep-0008/

        Crie variáveis com letras minúsculas, podendo ser inserido, após, números e underline;

        O sinal de igual (=) é o operador de atribuição;

        Exemplo de variável: 
        
            ↪ nome = expressao

            (Formato "snake case")
            ↪ nome_composto = expressao_valor

    As variáveis recebem qualquer valor.
    Quando atribuimos valores primitivos às variáveis, estamos nos referindo a valores literais.
    Variáveis não são utilizadas para abreviar código, são utilizadas para tornar o código mais legível.

"""

nome_completo = 'Erick Ferreira'
print(nome_completo)

soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

int_um = int('1')
print(int_um, type(int_um))


nome = 'Erick'
idade = 39
maior_idade = idade >= 18

print('Nome:', nome, 'tem', idade, 'anos')
print('É maior de idade:', 'Sim' if maior_idade else 'Não')
