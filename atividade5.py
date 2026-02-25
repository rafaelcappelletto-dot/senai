nome =input("Escreva o seu nome: ")

idade =int(input("Escreva a sua idade: "))

while idade >=120 or idade < 0:
    idade =int(input("Escreva a sua idade: "))

dias_vida = idade * 365
print(f"{nome}, você ja viveu {dias_vida} dias")

