#a turma do p1 precisa eleger um representante da sala. a eleição contem
#apenas 3 candidatos para serem votados pelos 55 alunos. Construa um algoritimo para ler o nome e receber os votos
def max_votes(x,y,z):
    if x > y and (y > z or z > y):
        return f'{c1} com {x} votos'
    if y > x and (x > z or z > x):
        return f'{c2} com {y} votos'
    return f'{c3} com {z} votos'
    
c1 = input('qual o primeiro candidato que você vai escolher')
c2 = input('segundo candidato?')
c3 = input('o último candidato')
v1 = 0
v2 = 0
v3 = 0
for k in range(55):
    while True:
        try:
            voto = int(input('escolha o número do candidato que você irá votar.'))
            if voto < 0 and voto > 3:
                continue
            else:
                break
        except ValueError:
            print('diga um número válido')
    if voto == 1:
        v1 +=1
    elif voto == 2:
        v2 +=1
    elif voto == 3:
        v3 +=1
print(f'o(a) representante da turma será {max_votes(v1,v2,v3)}')