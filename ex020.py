from random import randint
lista = []
for x in range(1,5):
    nome = str(input("Digite o {}º nome: ".format(x)))
    lista.append(nome)
for y in range(1,5):
    sorteado = randint(0,4-y)
    print(lista[sorteado])
    lista.pop(sorteado)