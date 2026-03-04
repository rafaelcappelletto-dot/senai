#Uma máquina mede a temperatura de um forno 10 vezes durante o dia.
#Crie um algoritmo que:
#Leia as 10 temperaturas
#Informe:
#A maior temperatura
#A menor temperatura
#A média das temperaturas
#Quantas vezes a temperatura ultrapassou 100°C

maior = float(0)
menor = float(0)
acima_cem = int(0)
soma = float(0)

#verificando a temperatura do forno 10 vezes
for cont in range(10):

    temp = float(input(f"Informe a {cont+1} temperatura do forno: "))
    
    #Dando um valor base para as variaveis
    if cont == 0:
        maior = temp
        menor = temp

    #Escolhendo a maior temperatura
    if temp > maior:
        maior = temp
    
    #escolhendo a menor temperatura
    if temp < menor:
        menor = temp

    #somando as temperaturas
    soma += temp

    #Verifiacando quantas vezes a temperatua ultrapassou 100 graus
    if temp > 100:
        acima_cem += 1

#Calculando a media
media = soma / 10

#Escrevendo os resultados
print("A maior temperatura é: ",maior)
print("A menor temperatura é: ",menor)
print("A média das temperaturas é: ",media)
print(f"A temperatura ultrapassou a marca de 100°: {acima_cem} vezes")

