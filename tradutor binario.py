
soma = 0
x = int(input('seu número binário'))
a = list(str(x))
for k in range(0,len(str(x))):
    if a[k] == '1':
        convertion = 1
    else:
        convertion = 0
    decimal = (2**k) * convertion
    soma += decimal
print(soma)