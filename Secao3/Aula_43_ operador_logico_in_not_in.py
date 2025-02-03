# Operadores in e not in
#strinf são interáveis
# 0 1 2 3 4 5 6
# G a b r i e l
# -7 -6 -5 -4 -3 -2 -1

nome= 'Gabriel'
print(nome[2])
print(nome[-6])

print('b'in nome)
print('Ga'in nome)
print(10*'-')
print('s'in nome)
print('briel'not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
