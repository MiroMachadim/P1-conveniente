def is_prime(numbers): #criando uma função
    if numbers==2: #number é so uma referencia,pode ser qualquer variável que você escolher fora da definição
        return True #comando return diz o que a função deve fazer, você pode colocar operações, strings e tudo mais dentro dele
    for number in range(2,numbers):
        if numbers % number == 0: #um número primo so pode ser dividido por 1 e ele mesmo, então se der resto 0 para algum número entre 2 e numbers-1, ele não é primo
            return False
    return True #quando se usa uma função, ela tem sistema de hierarquia similar ao elif, então se a primeira ou segunda opção funcionar,esse return será ignorado
x = int(input('digite um número'))
if is_prime(x): #não se precisa botar == True, já que a função feita ja vai definir como verdadeiro
    print('é primo')
else:
    print('não é primo')