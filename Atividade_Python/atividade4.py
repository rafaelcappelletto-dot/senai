n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = (n1+n2+n3+n4)/4

print(f"Sua média final é {media}")

# dizendo para o usuario se ele esta aprovado ou reprovado
if media >=7:
    print("Você está APROVADO!")
else:
    print("Você está REPROVADO!")
