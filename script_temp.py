#!/usr/bin/env python3

#1)Pedindo input da temperatura
input0 = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

#2)Verificando temperaturas fornecidas
input1 = input0.replace(",",".")
lista = input1.split()
#print("lista: ",lista)

    #2.1)Lista de testes para somente aceitar "-", "." ou "," além de números na entrada
listat0 = input1.replace("-","")
listat0 = listat0.replace(".","")
listat = listat0.split()
#print("lista teste: ",listat)

    #2.2)Testando valores de temperatura
for i in listat:
    indice = listat.index(i)
    valor = i
    temp = float(lista[indice])
    if valor.isdigit():
        ok = "ok"
    else:
        print("Insira valores numéricos de temperatura em °C")
        quit()

    #2.3)Testando se após cada "-" o próximo elemento do input é numérico
input_neg = input1
loc_neg = input_neg.find("-")

while loc_neg > 0:
    if input_neg[loc_neg+1].isdigit():
        ok = "ok!"
    else:
        print("Foi recohecido um caractere não numérico após algum - da sua entrada. Insira os dados novamente")
        quit()
    input_neg = input_neg[:loc_neg]+input_neg[loc_neg+1:]
    loc_neg = input_neg.find("-")

    #2.4)Testando se após cada "." ou "," o próximo elemento do input é numérico
input_dot = input1
loc_dot = input_dot.find(".")

while loc_dot > 0:
    if input_dot[loc_dot+1].isdigit():
        ok = "okay!"
    else:
        print("Foi reconhecido um caractere não numérico após algum . da sua entrada. Insira os dados novamente")
        quit()
    input_dot = input_dot[:loc_dot]+input_dot[loc_dot+1:]
    loc_dot = input_dot.find(".")


#Calculando as temperaturas em °F (e impedindo valores abaixo do zero absoluto!)
listaf = []

for j in lista:
    indice = lista.index(j)
    temp_c = float(lista[indice])
    temp_f = (9/5)*temp_c+32
    listaf.append(temp_f)
    if temp_c < -273.15:
        print("Alguma das temperaturas está abaixo do zero absoluto (-273.15°C)!")
        quit()

#Exibindo as temperaturas convertidas
print("{:<10} {:<10}".format("°C", "°F"))
for m in listaf:
    indice = listaf.index(m)
    print("{:<10} {:<10.2f}".format(lista[indice], m))
