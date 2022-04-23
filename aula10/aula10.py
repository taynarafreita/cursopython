""" Condições: IF, ELIF e ELSE"""
# Os 4 espaços abaixo do tipo de condição é para identificar que o oq estou escrevendo faz parte daquela condição.
# As condições são como se fosse "mãe" e o que colocamos dentro dela os "filhos".
# Só retorna os resultados verdadeiros, não retornam resultados falsos.
# Ele retorna o primeiro resultado verdadeiro que encontrar.

if False:
    print("Verdadeiro.")
    print("teste teste")
elif True:
    print("Agora é verdadeiro.")
    nome = input("Qual o seu nome? ")

    print(f'Seu nome é {nome}.')
elif False:
    print("Mais uma verdadeira.")
    print(22+22)
else:
    print("Não é verdadeiro.")
    print("Olá!")
