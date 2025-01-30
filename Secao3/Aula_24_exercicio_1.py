nome = str(input('Qual é o seu nome: '))
sobrenome =str(input('Qual é o seu Sobrenome: '))
idade= int(input('Qual sua idade: '))
ano_de_Nascimento= str(input('Qual é o ano do seu nascimento: '))
e_maior_de_Idade = idade >= 18
altura = float(input('Qual é sua altura: '))

maior_de_idade = "sim" if e_maior_de_Idade else "não"

print('Seu Nome é: {}\nseu sobrenome: {}\nsua idade: {}\nSeu ano de nascimento: {}\nÉ maior de idade? {}\nSua altura é de: {}'
      .format(nome, sobrenome, idade, ano_de_Nascimento, maior_de_idade, altura))