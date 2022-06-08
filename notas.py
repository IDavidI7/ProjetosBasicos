nota=int(input('Digite a nota do aluno para saber o conceito:  '))
while nota < 0 or nota > 100:
    print('Valor inválido!!')
    nota = int(input('Digite a nota do aluno para saber o conceito:  '))
if nota == 0:
    print('O aluno tirou "E"')
elif nota > 0 and nota < 36:
    print(' O aluno tirou "D"')
elif nota > 35 and nota < 61:
    print(' O aluno tirou "C"')
elif nota > 60 and nota < 86:
    print(' O aluno tirou "B"')
elif nota > 85 and nota <= 100:
    print(' O aluno tirou "A"')
