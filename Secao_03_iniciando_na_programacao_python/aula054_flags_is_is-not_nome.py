"""
    — Flag (bandeira): Marca um local
    
        None        -> Não valor
        is e is not -> É ou não é (tipo, valor, identidade)
        id          -> Identidade

"""

condicao = True
passou_no_if = None

if condicao:
    print('Faça algo')
    passou_no_if = True
else:
    print('Não faça algo')

print('Não passou no "if":', passou_no_if is None)