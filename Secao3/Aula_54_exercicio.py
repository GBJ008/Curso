'''
faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
numero_str = input('Digite um número: ')

if numero_str.isdigit():
    numero_int= int(numero_str)
    par_impar= numero_int % 2 == 0
    par_impar_texto= 'impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'o número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')