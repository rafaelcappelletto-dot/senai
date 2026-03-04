#Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
#a)  o novo peso se a pessoa engordar 15% sobre o peso digitado;
#b)  o novo peso se a pessoa emagrecer 20% sobre o peso digitado.
peso =0

while peso <=0 or peso > 600:
    peso = float(input("Digite seu peso atual: "))


peso_engordar = peso + (0.15*peso)
peso_emagrecer = peso - (0.20*peso)

print("Se você engordar 15 porcento a mais em relação ao seu peso, seu novo peso será: ",peso_engordar)
print("Se você emagrecer 20 porcento a mais, seu novo peso será: ",peso_emagrecer)