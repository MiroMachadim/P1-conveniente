#fazendo derivada,5x² = 10x
def elevado(x):
    if ord(x) == 179:
        return 178 
    elif ord(x) == 178:
        return 185
    return 1
digitos = 1
elevados = []
letra = []
expressao = input('qual expressão você vai converter para sua derivada?')
for termo in expressao:
    if ord(termo) in range(48,58):
        digitos *= int(termo)
    elif ord(termo) in (179,178,185):
        elevados.append(chr(elevado(termo)))
        if termo != '¹':
            digitos *= int(chr(ord(termo)-128))    
        else:
            digitos *= 1
    elif termo.isalpha():

        letra.append(termo)
if not letra:
    print(0)
elif elevados[0] != 1:
    print(str(digitos) + ''.join(letra) + ''.join(elevados))
elif elevados[0] == 1:
    print(digitos)
