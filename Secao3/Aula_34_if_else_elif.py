#if/ elif/else
# se/se não se /se não
entrada= str(input('Você quer "Entrar" ou "Sair"? '))

if entrada =='Entrar':
    print('Você entrou no sistema')
    print('Seja Bem-vindo!!!')
elif entrada == 'Sair':
    print('Você saio do sistema')
else:# o else sempre será a ultima opção( fechamento da função)
    print('Você não digitou nada!')

