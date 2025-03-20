soma = 0
x = input('seu número binário')
for k in range(1,len(x)+1):
    if x[-k] == '1':
        convertion = 1
    else:
        convertion = 0
    decimal = (2**(k-1)) * convertion
    soma += decimal
print(soma)