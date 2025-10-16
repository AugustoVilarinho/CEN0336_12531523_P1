#!/usr/bin/env python3
import sys

#Importando e verificando elementos da sys

    #Sequência de DNA
sequencia = sys.argv[1].upper() 
#print("A sequência é: {}".format(sequencia))

conjunto_teste = set(sequencia)
conjunto_ref = {"A","T","C","G"}
comprimento = len(sequencia)

if conjunto_teste.issubset(conjunto_ref) and conjunto_teste:
    print("A sequência de DNA é: {}".format(sequencia))
else:
    print("Você deve inserir uma sequência válida de DNA como primeira entrada")
    quit()

    #n_1 a n_6
lista_n = []

for i in range(6):
    valor = sys.argv[i+2]
    if valor.isdigit() and int(valor) < comprimento:
        #print("n_{}: {}".format(i+1,valor))
        lista_n.append(int(valor))
    else:
        print("Você deve inserir em sequência a sua sequência de DNA e n_1 a n_6, tente novamente")
        quit()
#Adicionando um elemento a mais na lista para trabalhar com índice 6
lista_n.append(0)
#print(lista_n)

#Definindo as sequências de teste GT e AG
seq_GT = "GT"
seq_AG = "AG"

#Extraindo seqûencia entre CDS1 e CDS2
seq_n2_n3 = sequencia[lista_n[1]:lista_n[3]+1]
#print(seq_n2_n3)

teste_23_1 = seq_n2_n3[0]+seq_n2_n3[1]
teste_23_2 = seq_n2_n3[-2]+seq_n2_n3[-1]

if teste_23_1 != seq_GT or teste_23_2 != seq_AG:
    print("A sequência entre CDS1 e CDS2 é inválida, tente conferir os valores de n_2 e n_3")
    quit()

#Extraindo seqûencia entre CDS2 e CDS3
seq_n4_n5 = sequencia[lista_n[3]:lista_n[5]+1]
#print(seq_n4_n5)

teste_45_1 = seq_n4_n5[0]+seq_n4_n5[1]
teste_45_2 = seq_n4_n5[-2]+seq_n4_n5[-1]

if teste_45_1 != seq_GT or teste_45_2 != seq_AG:
    print("A sequência entre CDS2 e CDS3 é inválida, tente conferir os valores de n_4 e n_5")
    quit()

#Criando a concatenação de CDS1, CDS2 e CDS3
CDS1 = sequencia[lista_n[0]:lista_n[2]+1]
CDS2 = sequencia[lista_n[2]:lista_n[4]+1]
CDS3 = sequencia[lista_n[4]:lista_n[6]+1]
seq_CDS123 = CDS1 + CDS2 + CDS3
print("A sequência formada por CDS1, CDS2 e CDS3 é: {}".format(seq_CDS123))
