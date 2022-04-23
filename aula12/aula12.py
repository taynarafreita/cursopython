'''' Operadores Lógicos: and, or, not, in e not in.'''

 # and só retorna verdadeiro se todas as comparações forem verdadeiras, caso contrário retornará falso.
 # or  retorna com verdadeiro se alguma for verdadeiro.
 # not inverte... é como o se não.
 # in checa se tal valor existe dentro do que foi colocado.
 # not in checa o inverso de in.


usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'taynara'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')

nome = 'Taynara'

#if 'b' not in nome:
    #print('Existe.')
#else:
    #print('Não existe.')

