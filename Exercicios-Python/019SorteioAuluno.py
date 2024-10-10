import random
print('------------- Nome dos alunos -------------')
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo Aluno: '))
p3 = str(input('Terceiro Aluno: '))
p4 = str(input('Quarto Aluno: '))
p5 = str(input('Quinto Aluno: '))
p6 = str(input('Sexto Aluno: '))

list = [p1, p2, p3, p4, p5, p6]
sort = random.choice(list)
print('O aluno sorteado foi {}'.format(sort))
