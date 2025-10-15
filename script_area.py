#!/usr/bin/env python3
import sys

#Importanto, convertendo para inteiros e testando os valores dos catetos
x = sys.argv[1]
y = sys.argv[2] 

if x.isdigit() and y.isdigit():
    print("Os catetos são a={} e b={}".format(x,y))
else:
    print("Você deve inserir um valor inteiro para os catetos")
    quit()

x = int(x)
y = int(y)

if x > 500 or y > 500:
    print("Você deve inserir valores inteiros entre 1 e 500 para os catetos")
    quit()

if x < 1 or y < 1:
    print("Você deve inserir valores inteiros entre 1 e 500 para os catetos")
    quit()

#Calculando e exibindo a área
area = (x*y)/2
area = int(area)
print("A área do triangulo retângulo com lados a={} e b={}, é {}".format(x,y,area))
