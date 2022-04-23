''' Formatando valores com modificadores'''

# Para formatar string usa-se -> :s Texto - strings;
# Para formatar um numero inteiro usa-se -> :d Inteiros - int;
# Para formatar numeros de ponto flutuante usa-se -> :f Ponto flutuante - float
# Para formatar casas decimais usa-se :.(numero)f - Casas decimais
# : (Caractere) (< ou > ou ^) (quantidade) (tipo - s, d ou f)
# > - Acrescenta na esquerda
# < - Acrescenta na direita
# ^ - Acrescenta no centro

num_1 = 1

print(f'{num_1}')

print(f'{num_1:0<5}')

print(f'{num_1:.2f}')

nome = 'Taynara freita'
nome_formatado = '{n} {n} {n}'.format(n=nome)
nome_formatado1 = '{}'.format(nome)


print(nome_formatado)
print(nome_formatado1)
print(nome.lower())
print(nome.upper())
print(nome.title())




