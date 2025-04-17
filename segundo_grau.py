#formula geral: ax**2 +bx +c
a = int(input('o valor de a?'))
if a == 0:
    print('isso não é uma uma equação do segundo grau, obrigado por usar o programa')
else:
    b = int(input('o valor de b?'))
    c = int(input('o valor de c?'))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('não existe valor de x')
    else:
        x1 = (-b+(delta**(1/2)))//(2*a) #ordem dos parentesis:2*a, delta**1/2, -b + resultado de delta**1/2, divisão no final
        x2 = (-b-(delta**(1/2)))//(2*a)
        if delta == 0:
            print(x1) #tanto x1 quanto x2 faria o mesmo resultado
        elif delta >0:
            print(x1,x2)