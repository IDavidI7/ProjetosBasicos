itens='lápis',2,\
    'caneta',3,\
    'caderno',12.90,\
    'mochila',55.90,\
    'corretivo',5,\
    'borracha',1,\
    'livro',34.90,\
    'óculos',30.59,\
    'garrafa',15.19,\
    'sua mãe', 2.50,\
print('='*40)
print(f'{"Tabela de preços":^40}')
print('='*40)
for pos in range(0, len(itens)):
    if pos %2 == 0:
        print(f'{itens[pos]:<31}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')