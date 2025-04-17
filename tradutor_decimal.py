binario = ''
n = int(input('seu número decimal: '))
while n > 1:
    binario += str(n%2)
    n =n // 2
binario += str(n)
print(binario[::-1])

