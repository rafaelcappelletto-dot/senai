cont = 0
soma =0

while cont < 4:
    cont +=1
   
    nota = float(input(f"Digite sua {cont} nota: "))

    if nota >= 0 and nota <= 10:
        soma += nota
    else:
        print("Nota Invalida")
        cont-=1

media = soma /cont

print(f"Sua média final é: {media}")
