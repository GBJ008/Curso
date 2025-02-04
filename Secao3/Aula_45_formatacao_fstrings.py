'''
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
<- Direita
^ - centro
= - força o número a aparecer antes do zeros
Sinal - + ou -
ex.: 0>-100,.1f
conversions flags - !r !s !a
'''
variavel ='ABCD'
print(f'{variavel}')
print(f'{variavel:_>10}')
print(f'{variavel:_^10}')
print(f'{variavel:_<10}')
print(f'{1000.12342342123123:,.1f}')
print(f'{1000.12342342123123:.1f}')
print(f'{1000.12342342123123:.1f}')
print(f'{-1000.12342342123123:-.1f}')
print(f'{1000.12342342123123:0=+10,.1f}')