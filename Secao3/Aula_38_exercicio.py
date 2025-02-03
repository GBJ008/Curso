primeiro_valor= input('Digite um valor: ')
segundo_valor= input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'o Primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'o Primeiro valor: {segundo_valor} é maior que o segundo valor: {primeiro_valor}')
else:
    print('Os Valores são iguais')