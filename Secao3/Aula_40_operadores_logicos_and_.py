# Operadores lógicos
#and(e) or (ou) not(não)
#and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a exepressão inteira será avaliada naquele valor 
# são considerados falsy (que você já viu)
#0 0.0 '' False
# também existe o tipo None  que é usado para representar um não valor

entra = input('[E]ntrar [S]air: ')

senha= input('Senha:')

senha_acesso = '1997'

#if só vai ser executado ser for True
if entra == 'E' and senha == senha_acesso:
    print('Entrada')
    print('Senha correta')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)