""" Entrada de Dados """

print('A função "input" sempre considera a classe como str, independente se colocou um número ou não.')
print('A função "input" serve para perguntar para o usuário.')
print('Se não colocar um espaço ao final da pergunta da função input, o texto fica colado.')
print('Para que seja possível fazer contas usando "input", é necessário converter a classe para int ou float.')
print('O nome cast é usado para se referir à conversão de variáveis para int, str, etc.')
print()

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nasc = 2021 - int(idade)
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))

print()
print(f'Exemplo 1: O usuário digitou {nome} e o tipo de varíavel é {type(nome)}.')
print()
print(f'Exemplo 2: {nome} tem {idade} anos.')
print()
print(f'Exemplo 3: {nome} nasceu em {ano_nasc}.')
print()
print(numero_1 + numero_2)