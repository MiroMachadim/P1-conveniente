def dANDr(x): 
    #informação das equações
    letters = []
    numberscount = []
    misc = []
    signal = []
    #pegando as informações
    for Ascii in x:
        if Ascii == '²' or Ascii == f'(' or Ascii == f')':
            misc.append(Ascii)
        elif Ascii == '+' or Ascii == '-':
            signal.append(Ascii)
        elif Ascii.isdigit():
            numberscount.append(Ascii)
        elif Ascii.isalpha():
            letters.append(Ascii)
    #a,b,c
    a = int(signal[0]+numberscount[0])
    if len(numberscount) >= 2:
        b = int(signal[1]+numberscount[1])
    if len(numberscount) >= 3:
        c = int(signal[2]+numberscount[2])
    #detectando que é segundo grau,ax²+bx+c
    if len(letters) == 2 and len(numberscount) >= 3 and len(misc) == 1:
        delta = b**2 - 4 * a * c
        if delta <= 0:
            return x
        x1 = (-b+(delta**(1/2)))/(2*a)
        x2 = (-b-(delta**(1/2)))/(2*a)
        return f'{a}({letters[0]}-{round(x1,2)})*({letters[0]}-{round(x2,2)})'
    #detectando que é quadrado da diferença,x²-a
    if len(letters) == 1 and len(misc) == 1 and len(numberscount) == 1 and (int(numberscount[0]) ** (1/2)) % 1 == 0:
        return f'({letters[0]}+{a**(1/2)}) * ({letters[0]}-{a**(1/2)})'
    #detectando que é produto notável,(x+a)²
    if len(letters) == 1 and len(misc) == 3 and len(numberscount) == 1:
        return f'{letters[0]}² + 2*{letters[0]}*{a} +{a}²'
    #nenhum caso
    return x
n = input('que equação você irá reescrever?')
print(dANDr(n))