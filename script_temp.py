#!/usr/bin/env python3

#Pedindo input da temperatura
input0 = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

#Verificando temperaturas fornecidas
lista = input0.split()
#print(lista)

    #Lista de testes para aceitar valores negativos
listat = input0.replace("-","")
listat = listat.split()
#print(listat)

    #Testando valores de temperatura
for i in listat:
    indice = listat.index(i)
    valor = i
    temp = int(lista[indice])
    if valor.isdigit():
        print("Temperatura {}: {}".format(indice+1,temp))
    else:
        print("Insira valores inteiros de temperatura em °C")
        quit()

#Calculando as temperaturas em °F
listaf = []

for j in lista:
    indice = lista.index(j)
    temp_c = int(lista[indice])
    temp_f = (9/5)*temp_c+32
    listaf.append(temp_f)

#Exibindo as temperaturas convertidas
print("°C   °F")
for m in listaf:
    indice = listaf.index(m)
    print("{}   {}".format(lista[indice],listaf[indice]))
