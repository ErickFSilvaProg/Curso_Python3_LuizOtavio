"""
    — Constantes em Python:
    
        Constante em Python é um valor fixo que não deve ser alterado durante a execução de um programa, indicado por convenção através de nomes escritos totalmente em letras maiúsculas.
        
        Sem restrição técnica nativa:
            Python não impede tecnicamente que você mude o valor de uma constante.
            
        Acordo de programadores:
            A comunidade usa letras maiúsculas com underscores (estilo SNAKE_CASE) para sinalizar que o valor é fixo e não deve ser modificado.

"""

# Velocidade atual do carro:
velocidade = 61

# Local em que o carro está na estrada:
local_carro = 99


# Velocidade máxima do radar 1:
RADAR_1 = 60

# Local onde o radar 1 está:
LOCAL_1 = 100

# A distância onde o radar pega:
RADAR_RANGE = 1


# *******************************************
if velocidade > RADAR_1 and \
    local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE):
        print('Carro multado em radar 1')
        print('Carro passou da velocidade no radar 1')

print()