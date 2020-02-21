import random

print("-----------------------------------------")
print("_______________________")
print("Sorteio Mega Sena      ")
print("_______________________")

print("Escolha 6 Numeros.    ")
print("______________________")
print("Voçe Ganha Se Açertar No Minimo 4 Numeros")
print("-----------------------------------------")


#lista dos numeros escolhidos
aposta = set()
#lista dos numeros sorteados
sorte = set()



#loop da aposta

for i in range(1, 7):
    ap = int(input("Informe o {}° Numero da Aposta : ".format(i)))
    aposta.add(ap)

print("------++--------------------------------------------")
#loop da sorteio
dec = int(input("Aperte o Numero 1 Para Iniciar o Sorteio :"))
if dec == 1 :
    while len(sorte) != 6:
        sto = random.randint(1,10)
        if sto not in sorte:
            sorte.add(sto)


#imprimir os resultados

print("------------\/-------------")
print("Numeros Da Aposta : {}".format(aposta))
print("Numeros Sorteados Sao : {} ".format(sorte))

print("Acertos : ",aposta.intersection(sorte))
print("Voçe Fez {} pontos".format(len(aposta.intersection(sorte))))


#condiçao simples da quantidade de pontos


if len(aposta.intersection(sorte)) >= 4 :
    print("Parabens Voçe Ganhou uma Parte Do Premio")
    print("----------/\---------------")
else:
    print("Voçe nao Acertou o Minimo de Pontos")  
    print ("------- /\------------------------")  
