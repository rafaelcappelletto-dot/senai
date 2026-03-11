#Um sistema mede a corrente elétrica (em amperes) de um motor 8 vezes.
#Crie um programa que:
#Leia as 8 medições
#Informe:
#Quantas estão acima de 15A
#Se houve sobrecarga (acima de 20A)
#A média da corrente
#Exibir alerta se alguma medição ultrapassar 200 PSI

acima_15 = 0
acima_20 =0
soma =0


for cont in range(8):

    corrente = int(input(f"Escreva a {cont+1} medição da corrente eletrica:"))

    if corrente > 15:
        acima_15 += 1

    if corrente > 20:
        acima_20 += 1

    if corrente > 200:
        print("ALERTA! A corrente ultrapassou 200")

    soma += corrente

media =soma/cont

print(f"A corrente ficou acima de 15: {acima_15} vezes")
print(f"Houve sobrecarga (acima de 20): {acima_20} vezes")
print(f"A média das corrente é igual: {media}")