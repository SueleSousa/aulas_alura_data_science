#%% ALURA 

#Introdução ao NUMPY

#%% Aula 1 - Vídeo 5 - O que são arrays Numpy?

import numpy as np

km = np.loadtxt(r"C:\Users\SUELESUSANFEITOSASOU\Desktop\data\carros-km.txt")
ano = np.loadtxt(r"C:\Users\SUELESUSANFEITOSASOU\Desktop\data\carros-anos.txt", dtype = int)

km_media = km/(2019-ano)
type(km_media)

#%% Aula 2 - Vídeo 2 - Operações matemáticas

a = 10/3
print(a)

# Número inteiro da divisão

b= 10//3
print(b)

# Mostra apenas o resto da divisão, no caso abaizo, conseguimos dividir 3 partes de 10 e sobra 1. 
c= 10%3
print(c)

# Exercício

d = 10 % 2 + 3 // 10
e = 5 * (2 + 3) / 2
f = 2 ** 3 * 4
print(d, e, f)

#%% Aula 2 - Vídeo 4 - Entendendo variáveis

ano_atual = 2019
ano_fabricacao = 2003
km_total = 44410

km_media = km_total / (ano_atual - ano_fabricacao)
print (km_media)

km_total = km_total + km_media
print(km_total)

# Declaração Múltipla

ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410

print (ano_atual, ano_fabricacao, km_total)

#%% Aula 2 - Vídeo 7 - Tipos de Dados

nome = "Suele Sousa"
print(type(nome))
nome2 = "Suele 'Sousa'"
print(nome2)
carro = '''
nome
idade
nota
'''
print(type(carro))

#%% Aula 2 - Vídeo 9 - Conversão de Tipos

a = 10
b = 20
c = "Python é "
d = "legal."

print(a + b)
print(c + d)
print(c + str(a)) 
print(float(a))

var = 3.143839

print(int(var))


text = 'A quilometragem média do veículo é '
Km = 100000
Ano_atual = 2019
Ano_fabricacao = 1999

print(text + str( int( Km / (Ano_atual - Ano_fabricacao) ) ) + ' km')

#%% Aula 2 - Vídeo 11 - Conversão de Tipos

print("Olá,  {}! Esse é seu acesso de número {}.".format("Rodrigo", 32))

print("Olá, {nome}! Esse é seu acesso de número {acesso}.".format(nome = "Rodrigo", acesso =32))

nome = "Rodrigo"
acesso = 32

print(f"Olá {nome}, seu número de acesso é {acesso}.")