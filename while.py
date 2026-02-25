cont = 0
soma = 0

# Pedindo a nota do usuario enquanto a o cont < 4
while cont < 4:

    cont += 1
    
    # Pedidindo para o ususario inserir suas notas
    nota = float(input(f"Digite a nota {cont} : "))

    # Verificando se o usuario escreveu uma nota valida
    if nota >= 0 and nota <= 10:
        soma += nota
    else:
        print("Nota Invalida")
        cont -= 1

media = soma /cont

# escrendo a media no terminal
print(f"Sua média final é: {media}")

# dizendo para o usuario se ele esta aprovado ou reprovado
if media >=7:
    print("Você está APROVADO!")
else:
    print("Você está REPROVADO!")



