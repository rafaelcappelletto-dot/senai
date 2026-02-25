nome =input("Escreva o seu nome: ")

idade =int(input("Escreva a sua idade: "))

if idade <=120 and idade > 0:
    dias_vida = idade * 365
    print(f"Você ja viveu {dias_vida} dias")
else:
    print("Idade invalida")
