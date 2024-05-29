#inserindo variaveis

K = float(input('Digite o valor da constante: '))
X = float(input('Digite o valor da distância: '))

#Inserindo Formula

E = K * X ** 2 / 2

#Condicao

if E <= 100:
  print('A energia se manteve constante')
elif E >= 100:
  print('A energia aumentou consideravelmente')
else:
  print('A energia teve um aumento fora do normal')

#Imprimindo o valor da energia

print(f'Digite o valor : {E} J ')