
soma = 0
x = input('seu número binário')
for k in range(0,len(x)):
    if x[k] == '1':
        convertion = 1
    else:
        convertion = 0
    decimal = (2**k) * convertion
    soma += decimal
print(soma)