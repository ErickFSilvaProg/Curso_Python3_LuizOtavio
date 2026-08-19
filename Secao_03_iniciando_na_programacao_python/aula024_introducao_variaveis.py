"""
    Váriáveis são utilizadas para salvar algo na memória do computador.

    Regras da PEP8: https://peps.python.org/pep-0008/

        Inicie variáveis com letras minúsculas, podendo utilizar números e underline;
        O sinal de igual (=) é o operador de atribuição;

        Exemplo de variável: 
        
            ↪ nome = expressao

            (Snake case)
            ↪ nome_composto = expressao_valor

    As variáveis recebem qualquer valor.
    Quando atribuimos valores primitivos as varipaveis, estamos nos referindo a valores literais.
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
