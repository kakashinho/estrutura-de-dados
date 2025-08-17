# Faça a seguinte lista de Listas, Dicionários e sort com key=
# Não use o chatgpt, tente fazer sozinho

# Seja uma lista de inteiros, mostre apenas os números pares usando list comprehension.
# comprehension = [conta | Domínio | Condição]
from random import sample
lista = sample(range(1,101), 10)

numeros = [x for x in lista if x % 2 == 0 ]
#print(numeros)

# Crie uma lista com os quadrados de todos os números pares de 1 a 20 usando list comprehension.
lista = [x**2 for x in range(1,21)]
#print(lista)

# Dada uma lista de palavras, ordene-a pelo tamanho das palavras em ordem crescente, utilizando sorted() com a cláusula key=.
nomes = 'ana maria caio rafael mateus beatriz julia'.split()
nomes = sorted(nomes, key=len)
#print(nomes)

# Dada uma lista de palavras, ordene-a pelo número de vogais presentes em cada palavra.
def contvogais(nome):
    vogais = 'aeiou'
    nome = nome.lower()
    cont = 0
    for x in nome:
        if x in vogais:
            cont += 1
    return cont

nomes = sorted(nomes, key=contvogais)
#Ordenando de forma crescente quantidades de vogais
#print(nomes) 

# Dada uma lista de palavras, ordene-a pelo último caractere de cada palavra.
nomes = sorted(nomes, key=lambda a: a[-1])

# Ou
def last(a): return a[-1]
nomes = sorted(nomes, key=last)
#print(nomes)

# Dada uma string, utilize list comprehension para criar uma nova string onde os caracteres aparecem alternando entre maiúsculas e minúsculas.
string = 'banana'
for k, x in enumerate(string):
    #print(k,x)
    pass

#Uma forma de fazer:
string = ''.join([x.upper() if k%2 == 0 else x.lower() for k,x in enumerate(string)])

#print(string)

# Dada uma lista de strings contendo números misturados com letras (por exemplo, "a3b", "z12y", "c1x"), ordene a lista com base no número contido na string.
lista = ["a3b", "z12y", "c1x"]
def valor(palavra):
    return int(''.join([x for x in palavra if x.isdigit()]))

lista = sorted(lista,key=valor, reverse=True)
print(lista)

# Crie um dicionário que mapeia os números de 1 a 10 para seus respectivos quadrados, usando dict comprehension.

#Declarando um dicionário:
dicionario = {
    'chave1':'valor1',
    'chave2':'valor2'
}

#Declarando o dicionário com seu quadrado:
dicionario = {x: x**2 for x in range(1,11)}
#print(dicionario)

# Dada uma string, crie um dicionário onde as chaves são os caracteres e os valores são a contagem de vezes que cada caractere aparece.
nomes = 'ana maria caio rafael mateus beatriz julia'.split()
nomes = ''.join(list(nomes))
dicionario = {x: nomes.count(x) for x in sorted(set(nomes))}

ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
print(ordenado)

'''Outros métodos de ordenação:
dict(sorted(dicionario.items(), key=itemgetter(1), reverse=True)), 
dict(contador.most_common()),
df.sort_values(ascending=False),
while temp:
    chave_max = max(temp, key=temp.get)
    ordenado[chave_max] = temp.pop(chave_max) 
'''


# Dado um dicionário qualquer, crie um novo dicionário onde as chaves e os valores estejam invertidos.

#revisão para prova o que são dicionários
alunos = {'ana': 9, 'julia': 7, 'miguel': 8, 'pedro': 5}
print({valor: chave for chave, valor in alunos.items()})

# Dado um dicionário de números, crie um novo dicionário contendo apenas os pares chave-valor onde o valor seja maior que um determinado número.
print({x: x for x in range(10) if x % 2 == 0})


# Dado um dicionário, ordene-o pelos valores e retorne uma lista de tuplas ordenadas.
print(sorted(dicionario.items(), reverse = True))

# Dado um dicionário onde as chaves são palavras, ordene-o com base no comprimento das chaves.
print(sorted(alunos.keys(), key=len, reverse= True))

# Dada uma frase, crie um dicionário onde as chaves são palavras e os valores são a contagem de vezes que cada palavra aparece.

texto = '''Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'''

texto = texto.replace(',', '')
texto = texto.replace('.', '')
texto = texto.replace('"', '')
import re
texto = re.sub(r'\d', '', texto)
texto = texto.lower()
texto = texto.split()
print()

print(sorted({x: texto.count(x) for x in set(texto)}.items(), key= lambda x :len(x[0]), reverse = True))
print(sorted({x: texto.count(x) for x in set(texto)}.items(), key= lambda x :x[1], reverse = True))


# Dado um dicionário onde os valores são números, crie um novo dicionário onde cada valor seja a raiz quadrada do original.
from random import sample
import math
lista = sample(range(1,1000),500)

#print(lista)

def quadrado(n):
    sqrt_n = math.isqrt(n)
    if n == int(sqrt_n**2):
        return sqrt_n**2
    
    return False

print(sorted({x: x for x in lista if quadrado(x)}.values()))

# Dada uma lista de palavras, crie um dicionário onde as chaves sejam as primeiras letras e os valores sejam listas das palavras correspondentes.
palavras = 'Contrary popular belief Lorem Ipsum is not simply random raw text'.lower().split()
print({x[0]: x for x in palavras})

# Dado um dicionário de números, ordene-o pelos valores em ordem decrescente e retorne uma lista de tuplas ordenadas.
novo= {
    1:100,
    2:80,
    3:15,
    4:30,
    }

print(sorted(novo.items(), key=lambda x: x[1], reverse = True))