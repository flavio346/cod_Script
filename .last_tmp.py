print("Calculo Porcentagem")
print("____________________")
print("$ Desconto")
print("$ Acreçimo")
print("____________________")


# loop do codigo

while True:

   p1 = int(input("Informe o Tipo do Calculo: | [1] Desconto [2] Acreçimo |:"))
   if p1.type != int:
       print("erro")
#condiçao e calculo do desconto
   if p1 == 1 :
       print("__________________________________")
       ds1 = int(input("Digite o Valor do Produto : "))
       ds2 = int(input("Digite o valor do desconto : "))
       
       mult = ds1 * ds2
       
       rst = mult / 100
       
       rsf = ds1 - rst
       
       print("O Desconto de {}% de {} é de : {} reais".format(ds2,ds1,rst))
       
       print("Valor do Produto com Desconto: {} reais".format(rsf))
       
       print("________________________________________")
#opçao de parar o loop
       
       p2 = input("Deseja Continuar [sim] ou [nao] : ")
       if p2 == "nao":
           break
   
# condiçao e calculo do acrecimo
   if p1 == 2 :
       print("__________________________________")
       ac1 = int(input("Digite o Valor Inicial :"))
       ac2 = int(input("Digite o Valor Final :"))
       
       sub = ac1 - ac2
       
       rst = abs(sub / ac1 )* 100
       
       print(" Acreçimo do Valor foi: {}%".format(rst))
       print("____________________________")
       
#opçao de parar o loop
       p2 = input("Deseja Continuar [sim] ou [nao]: ")
       if p2 == "nao":
           break