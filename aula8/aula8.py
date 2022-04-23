#Exercício

nome = 'Taynara'
idade = 24
altura = 1.58
peso = 50.2
ano = 2022
ano_nasc = ano - idade
imc = peso / altura ** 2


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é{imc: .2f}.')
print(f'{nome} nasceu em {ano_nasc}.')
