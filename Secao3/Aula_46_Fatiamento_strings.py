'''
Fatiamento de Strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p][::]
Obs: a Função len retorna a qtd de caractres da str
'''
variavel= 'Olá mundo'
print(variavel[4])
print(variavel[3])
print(variavel[4:8])
print(variavel[4:])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[:5])

#len= ajuda a contar caracteres
print('1',len(variavel))

print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[0:9:3])
print(variavel[0:9:1])
#pega a str ao contrário 
print(variavel[-1:-10:-1])