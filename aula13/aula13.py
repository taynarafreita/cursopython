''' Caracteres de uma string
'''

# A função "len" não funciona com int, float e nem bool, somente string.

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(f'"{usuario}" possui {qtd_caracteres} caracteres e seu tipo é {type(qtd_caracteres)}')


if qtd_caracteres < 7:
    print('Você precisa digitar pelo menos 7 caracteres.')
else:
    print('Você foi cadastrado no sistema.')