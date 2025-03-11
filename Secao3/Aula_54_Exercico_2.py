'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apriada. Ex.
Bom Dia 0-11, Boa Tarde 12_17 e boa noite 18_23
'''


hora = input('Digite o horário com um (.) ao invés de (:) ')
try:
    hora= float(hora)
    hora= float(hora)
    if (hora >= 0 and hora <= 11) :
        print('Bom dia')

    elif (hora >= 12 and hora<= 17):
         print('Boa Tarde')

    elif (hora >= 18 and hora<= 23):
         print('Boa noite')

    else:
         print('Você digitou um horário inesistente ')
except:
     print('Você não digitou um número')