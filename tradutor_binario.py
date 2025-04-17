soma = 0
contador = 0
x = input('seu número binário')
for k in x[::-1]:
    if k == '1':
        decimal = (2**(contador)) * 1
        soma += decimal
    contador +=1
print(soma)
