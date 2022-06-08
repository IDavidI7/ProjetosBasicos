primo=int(input('Digite um número para saber se ele é um número inteiro e um número primo:  '))
divisao=0
for c in range(1,primo+1):
    if primo % c == 0:
        print('\033[31m', end=' ')
        divisao += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if divisao==2:
    print('\n\033[mfoi dividido {} vezes, por isso é um número primo.'.format(divisao))
else:
    print('\n\033[mfoi dividido {} vezes, por isso não é um número primo.'.format(divisao))
