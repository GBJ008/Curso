nome= input('Qual é o seu nome? ')
idade= input('Qual é a sua idade? ')
tem_espaco = ' 'in nome
espaco='Sim' if tem_espaco else 'Não'

invertido= (nome[len(nome):-100:-1])



letras= len(nome)


if len(nome) and len(idade):
    ultima_letra= nome[-1]
    primeira_letra= nome[0]
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {invertido}')
    print(f'Seu nome contém espaço? {espaco}')
    print(f'Seu nome tem {letras}')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A ultima letra do seu nome é {ultima_letra}')
else:
    print('Você não digitou nada!!')