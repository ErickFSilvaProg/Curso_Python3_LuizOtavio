"""
    — Introdução ao try/except:
    
        try    -> Tenta executar o código neste bloco.
        except -> Caso ocorra algum erro na execução do código, este bloco será executado.

        ↪ Forçando um erro do tipo ValueError:

            raise ValueError("Este é um erro forçado de valor inválido!")

            • raise: É o comando do Python usado para "levantar" ou lançar uma exceção de forma manual.
            • ValueError: É o tipo de exceção (você pode usar outros, como ZeroDivisionError, TypeError ou criar uma exceção personalizada).
            • A execução pula imediatamente para o bloco except assim que o raise é acionado.
        
    
    O método .isdigit() em Python verifica se uma string é composta exclusivamente por caracteres numéricos inteiros, retornando True se isso for verdade e False caso contrário.

    •● Como Funciona:

        Retorna True se a string não estiver vazia e contiver apenas números (de 0 a 9) ou caracteres Unicode que representam dígitos (como sobrescritos ²).
        
        Retorna False se houver letras, espaços, pontos decimais, sinais de negativo ou qualquer outro símbolo.
    
    •● Para que Serve:
    
        Validação de dados:
        
            Garantir que o usuário digitou apenas números antes de converter o valor com int().
            
        Limpeza de strings:
        
            Filtrar conteúdos em textos.

"""

# **************************************************************
another_number = input('Vou triplicar o número digitado: ')

try:

    if another_number.isdigit():

        another_number = float(another_number)
        doubled_number = another_number * 3
        
        print(f'O triplo de {another_number} é {doubled_number:.1f}')
    else:
        raise ValueError('Isso não é um número')
    
except ValueError as e:
    print(e)

print()