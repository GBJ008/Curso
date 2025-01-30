# Variáveis são usadas para salvar algo na memória do computador.
# pep8: Inicie variáveis com letras minúsculas, pode usar 
# underline _.
# o sinal de = é o operador de atribuição. Ele é usado para 
# atribuir um valor a um nome (variável).
# uso: nome_variavel = expressão
nome_completo = 'Gabriel Silva De Jesus'
soma_dois_mais_um = 2 + 2
int_um = int('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_um)
# bool
nome =  'Gabriel'
idade = 17
maior_de_idade = idade >= 18
print('Nome:{} Idade {} é menor ou maior {}'.format(nome, idade, maior_de_idade))
#teste pessoal
nome= str(input('Qual é o seu nome: '))
idade =int(input('Qual é sua idade: '))
e_maior_que_18 = idade >= 18 

print('Nome: {} Idade: {} \né maior de idade? {}'.format(nome, idade, e_maior_que_18))
