while True: #comece o comando criando um loop infinito, ele vai ser quebrado se for efetivado
    try: #o comando try significa tente, ele vai executar o comando mas ele vai se preparar para possiveis erros
        cds=int(input('quantos discos você possui?'))
        if cds < 0:
            raise ValueError from None #causando um ValueError de proposito, assim você não precisa criar mais de um print
        break #se nada der errado, sai do loop infinito e prossiga com o resto do codigo fora do while.
    except ValueError: #isso é uma ocasião caso a pessoa digite uma letra no input, que vai causar um ValueError
        print('insira uma quantidade de cds válida')