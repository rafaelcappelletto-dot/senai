nome = input("Digite seu nome: ")
print("Boas vinda,",nome)
continuar = True


while continuar == True:

    print("1 - Registrar uma entrada")
    print("2 - Registrar uma saida")
    
    operacao = int(input("R: "))

    if operacao == 1:
        print("entrada")
    elif operacao == 2:
        print("saida")

    else:
        print("Seleção invalida")


    continuar = input("Você deseja registrar outra operação? [S] ou [N]")

    if continuar == "S" or continuar == "s":
        continuar = True
    elif continuar == "N" or continuar == "n" :
        continuar = False
    else:
        print("Seleção invalida")
