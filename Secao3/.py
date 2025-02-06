nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
 
if len(nome) >= 1 and len(idade) >= 1:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[len(nome):-10000:-1]}")
 
    print(f'Seu nome contém espaços ? ', " " in nome)
    print(f"seu nome {nome} contém N° de {len(nome)} letras")
    print(f"A primeitra letra do seu nome: {nome[0]}")
    print(f"A última lerta do seu nome é: {nome[-1]}")
else:
    print("Você deixou algum campo vazio")