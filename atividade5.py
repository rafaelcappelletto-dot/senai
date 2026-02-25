#inserindo o nome do usuario
nome =input("Escreva o seu nome: ")

#gambiarra do krl
ano =121
mes =13
dia =31

# Só para enfeitar
print("_____________________________________________________________________________________")
print("Para descobrir quantos dias você ja viveu, escreva as seguintes informações")
print("_____________________________________________________________________________________")

#pedidno as informaçoes e impedindo que o ususario ultrapasse o limite
while ano >120:
    ano =int(input("Escreva o numero de anos que você ja viveu: "))
while mes > 12:
    mes =int(input("Escreva o numero de meses que você ja viveu: "))
while dia >30:
    dia =int(input("Escreva o numero de dias que você ja viveu: "))

# somando todos os dias
soma = (ano*365)+(mes*30)+dia

#Escrevendo o resultado final 
print(f"Seu nome é {nome} e você já viveu {soma} dias")

