#Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
#a)  o novo peso se a pessoa engordar 15% sobre o peso digitado;
#b)  o novo peso se a pessoa emagrecer 20% sobre o peso digitado.


peso = float(input("Digite seu peso atual: "))

while peso <=0 or peso > 600:
    peso = float(input("Digite seu peso atual: "))


peso_engordar = peso + (peso * 0.15)
peso_emagrecer = peso - (peso * 0.20)

print("Se você engordar 15 porcento a mais em relação ao seu peso, seu novo peso será: ",peso_engordar)
print("Se você emagrecer 20 porcento a mais em relação ao seu peso, seu novo peso será: ",peso_emagrecer)