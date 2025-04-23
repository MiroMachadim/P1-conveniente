#fazendo derivada,5x² = 10x
def elevado(x):
    if ord(x) == 179:
        return 178 
    elif ord(x) == 178:
        return 185
    return 1
digito = ''
switch = 0
digitos = 1
elevados = []
letra = []
expressao = input('qual expressão você vai converter para sua derivada?')
for termo in expressao:
    if ord(termo) in range(48,58) and switch == 0:
        digito += termo
        switch = 1
        continue
    elif ord(termo) in (179,178,185):
        elevados.append(chr(elevado(termo)))
        if termo != '¹':
            digitos *= int(chr(ord(termo)-128))    
        else:
            digitos *= 1
    elif termo.isalpha():
        letra.append(termo)
    if ord(termo) in range(48,58) and switch == 1:
        digito += termo
        print(digito)
        digitos *= int(digito)
        switch = 0
        digito = ''
    elif switch == 1:
        digitos *= int(digito)
        switch = 0
        digito = ''
        
if not letra:
    print(0)
elif elevados:
    print(str(digitos) + ''.join(letra) + ''.join(elevados))
elif not elevados:
    print(digitos)
