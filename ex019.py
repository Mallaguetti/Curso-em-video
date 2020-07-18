from random import randint
lista = []
for x in range(4):
    nome = str(input("Digite o {}º nome: ".format(x+1)))
    lista.append(nome)
print(lista[randint(0,3)])