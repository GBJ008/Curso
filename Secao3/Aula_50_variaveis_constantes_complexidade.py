''' 
COSTANTE= 'Variáveis' que não vão mudar 
Muitas condiçoes no mesmo if (Ruim)
  <-- contagem de complexidade (Ruim)

'''
velocidade= 61 #velocidade atual do carro
local_carro = 101 #local em que o carro está na estrada

RADAR_1= 60 # velocidade máxima do radas 1
LOCAL_1=  100 #local onde o radas 1 está
RADAR_RANGE = 1# A distância onde o radar pega

ranger_menos= local_carro - RADAR_RANGE
ranger_mais = local_carro + RADAR_RANGE
velocidade_carro_passou_radar_1= velocidade > RADAR_1
carro_passou_radar_1= (ranger_menos)and(ranger_mais)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade > RADAR_1:
    print('Está acima da velocidade!!')

if carro_multado_radar_1:
    print('Carro Passou no Radar 1')

if local_carro >=carro_passou_radar_1 and velocidade_carro_passou_radar_1 :

    print('carro multado em radar 1')
