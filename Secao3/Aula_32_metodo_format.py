strings= 'a={0} b={1} b={1} c={2:.2f}'
a ='A'
b= 'B'
c= 2.2

string= 'a={} b={} c={:.2f}'
stringss= 'a={0} b={1} b={1} c={nome3:.2f}'
formato= string.format(a,b,c)# . ajuda a mostras os metodos que pode ser utilizado
formatos= strings.format(a,b,c)
#nomeação
formatoss= stringss.format(a,b,nome3=c)

print(formato)
print(formatos)
print(formatoss)