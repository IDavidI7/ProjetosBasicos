#perguntas sobre o financiamento
valor_imovel=float(input('Qual o valor do imóvel?  R$'))
anos=float(input('Em quantos anos você deseja pagar?  '))
salario=float(input('Qual o seu salário?  R$'))
meses=anos*12
if salario*(30/100) < valor_imovel/meses:
    print('Infelismente o valor do seu salário não se encaixa com o valor proposto pelo banco.')
else:
    print('Parabéns, o valor foi aporvado pelo banco.')