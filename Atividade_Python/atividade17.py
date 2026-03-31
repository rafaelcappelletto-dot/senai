

print("Boas-vindas Rafael!")
print("horário comerical - 9h as 18h")

#pedindo o tipo de cliente para o usuario
tipo =input("insira se é um membro ou visitante: ").lower()


#verifcando qual opção o usuario escolheu
if tipo not in ["membro","visitante"]:
    print("Seleção invalida")

elif tipo == "membro":
    
    print("Acesso liberado!")
    
elif tipo == "visitante":#visitante

    #pedindo o quanto e quando o usuario deseja usar 
    ti = int(input("Digite a hora em que vocÊ deseja começar a usar: "))#tempo de inicio do uso
    tf = int(input("Digite a hora em que vocÊ deseja terminar de  usar: "))#tempo do termino do uso

    #verficando se a quantidade de horas que o usuario deseja usar e equivalente ao que ele pode usar
    if tf - ti <=4:
        #verificando se o horario esta dentro do horario comercial
        if  ti >= 9 and tf <=18:
            print("Acesso liberado ")
        else:
            print("Acesso negado - intervalo fora do horario comercial")

    else:
        print("Acesso negado - intervalo muito longo para seu tipo de usuario")
