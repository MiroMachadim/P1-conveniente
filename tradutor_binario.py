#variáveis iniciais, uma para a soma das conversões e outra para
#ser o número elevado
soma = 0
contador = 0
x = input('seu número binário')
for k in x[::-1]: #esse [::-1] é como se usa um reverse sem função(a pedido de erlon)
    if k == '1':
        decimal = (2**(contador)) * 1 #0 motivos para fazer isso quando não se é 1
        #então não tem praq decidir se é 1 ou 0
        soma += decimal
    contador +=1
    #o contador tem que ta fora do if, ja que o aumento acontece n importa se for 0 ou 1
print(soma)
