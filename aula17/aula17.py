''' Manipulando Strings'''

# Cada caractere de uma string tem um indice, que pode ser positivo ou negativo;
# o índice positivo começa do 0 e vai até o último caractere;
# o indice negativo começar do -9 e vai até o -1 (no exemplo do python s2)
# Para o python puxar o índice, é necessário utilizar os colchetes [] colocando o número do indice que deseja que rode.
#Fatiamento de Strings [inicio:fim:passo]: coloca a partir de onde até onde quer que retorne resultado. Ex abaixo:
#Para fatiar, usa-se dois pontos; o numero do indice q colocar primeiro é a partir de onde ele vai buscar e o que
#colocar em seguida é onde vai terminar, mas se quer que puxe o penultimo indice, deve colocar o ultimo indice pq ele
#não puxa o indice q foi colocado no fim, ele termina no anterior.
#se quer q puxe do inicio do indice, não precisa colocar nada no inicio pq o python vai entender que é pra puxar do inicio.
# O mesmo vale para se quiser que puxe até o ultimo indice.
# Tbm é possível fazer com que pule numeros da seguinte forma: [0:6:2]. Nesse exemplo, vai pular de dois em dois.


#positivos   [012345678]
texto      = 'Python s2'
#negativos  -[987654321]

#print(texto[2])

nova_string = texto[0:8]
print(nova_string)