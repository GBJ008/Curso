'''
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X- Hexadecimal(abcdef0123456789)
'''

nome = 'Gabriel'
preco= 1000.95897643
variavel= '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('o Hexadecimal de %d é %x' % (15, 15))