lista0 = []
lista1 = []
lista2 = []
lista3 = []
print('Primeira linha: ')
for c in range (3):
    num = int(input('Digite um número: '))
    lista1.append(num)
lista0.append(lista1)
print('Segunda linha: ')
for c in range (3):
    num = int(input('Digite um número: '))
    lista2.append(num)
lista0.append(lista2)
print('Terceira linha: ')
for c in range (3):
    num = int(input('Digite um número: '))
    lista3.append(num)
lista0.append(lista3)
print(lista0)
soma1 = lista1[0] + lista2[1] + lista3[2]
soma2 = lista1[2] + lista2[1] + lista3[0]
resultado = soma1 - soma2
'''print(resultado)
print(soma1)
print(soma2)'''
if resultado < 0:
    absoluto = resultado - resultado - resultado
    print(f'o valor absoluto das linhas diagonais é {absoluto}')
else:
    print(f'o valor absoluto das linhas diagonais é {resultado}')
