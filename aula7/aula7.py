nome = 'Taynara'
idade = 23
altura = 1.58
e_maior = idade > 18
peso = 50
imc = peso / altura ** 2


print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é{imc: .3f}')
print('{} tem {} anos de idade e seu IMC é {:.4f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
