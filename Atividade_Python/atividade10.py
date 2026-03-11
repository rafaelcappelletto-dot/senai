#Um sistema mede a corrente elétrica (em amperes) de um motor 8 vezes.
#Crie um programa que:
#Leia as 8 medições
#Informe:
#Quantas estão acima de 15A
#Se houve sobrecarga (acima de 20A)
#A média da corrente
#Exibir alerta se alguma medição ultrapassar 200 PSI

acima_15 = 0
acima_20 = 0
acima_200 = 0
sobrecarga = False
alerta = False
soma = 0

for i in range(8):

    corrente = float(input(f"Escreva a {i+1} medição da corrente eletrica:"))

    if corrente > 15:
        acima_15 += 1

    if corrente > 20:
        sobrecarga = True
        acima_20 += 1

    if corrente > 200:
        alerta = True
        acima_200 += 1
        print("ALERTA! A corrente ultrapassou 200")

    soma += corrente

#não colocar o [i] pq senao ele vai dividir por 9
media = soma/8

print(f"A corrente ficou acima de 15A: {acima_15} vezes")
if sobrecarga:
    print(f"Houve sobrecarga (acima de 20A): {acima_20} vezes")
if alerta:
    print(f"Houve alerta (acima de 200A): {acima_200} vezes")
print(f"A média das correntes é: {media} A")


