""" Operadores Relacionais: == > >= < <= !="""
# ==: perguntando se o valor é igual, não afirmando.
# !=: diferente
# Os demais sinais são conforme a matemática.

num_1 = 2
num_2 = 2

expressao = (num_1 != num_2)

#print(expressao)

var_1 = 'Taynara'
var_2 = 'Taynara'

expressao = (var_1 != var_2)

#print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)

# Limite para pegar o empréstimo
idade_limite = 18

#if idade >= idade_limite:
    #print(f'{nome} pode pegar o empréstimo.')
#else:
    #print(f'{nome} NÃO pode pegar o empréstimo.')

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

