'''
Introdução ao try/expect
try-> Tentar executar o código
except-> ocorreu algum erro ao tentar executar
'''
numero_str=input('Digite um número para eu dobrar: ')
#.isdigit= ele ve se foi só número digitados, só números inteiros 
# print(numero_str.isdigit())

# numero_float= float(numero_str)
# print(f'o dobro de {numero_str} é {numero_float * 2:.0f}')

'''
if numero_str.isdigit():
    numero_float= float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float *2:.2f}')
else:
    print('Isso não é um número')

    '''
#ele captura o erro e executa o expect

try:
    numero_float= float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print('Isso não é um número')