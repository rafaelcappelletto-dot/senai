
#mensagem de boas vindas
print("Boas-vindas Rafael!")
print("horário comerical - 9h as 18h")

#pedindo o tipo de cliente para o usuario
tipo =input("\ninsira se é um membro ou visitante: ").lower().strip()
dia = int(input("DIgite o dia da semana:\n1-Domingo\n2-Segunda\n3-Terça\n4-Quarta\n5-Quinta\n6-Sexta\n7-Sabádo\n: "))

#verifcando qual opção o usuario escolheu
if tipo not in ["membro","visitante"]:#opção invalida
    print("Seleção invalida")

elif tipo == "membro":#membro
    
    #verificando se é um dia util(9-18)
    if dia <7 and dia >1:
        #pedindo a hora atual 
        hora_atual = int(input("Digite o horário atual(arredondado): "))

        #verificando quantas horas o cliente ainda tem para usasr o site
        horas_restantes = 18 - hora_atual

        #verificando se a hora respondiada está dentro do horario comercial
        if hora_atual >=9 and hora_atual <18:
            print("Acesso liberado!")
            print(f"Você tem mais {horas_restantes} para usar o site!")
        else:
            print("Acesso negado - horário fora do horario comercial")
    else:#Liberando o acesso no final de semana inteiro
        print("Acesso liberado! - Final de semana")
    
elif tipo == "visitante":#visitante

    #perguntando o dia para o usuario para saber se ele pode acessar ou não
    dia = int(input("DIgite o dia da semana:\n1-Domingo\n2-Segunda\n3-Terça\n4-Quarta\n5-Quinta\n6-Sexta\n7-Sabádo\n: "))

    #verificando se o visitante pode acessar o site de acordo com o dia (não pode usar durante o final de semana)
    if dia < 7 and dia > 1:
        #pedindo o quanto o usuario deseja usar 
        hora_atual = int(input("Digite o horário atual(arredondado): "))#tempo de inicio do uso
        hora_final = int(input("Digite a hora em que vocÊ deseja terminar de  usar: "))#tempo do termino do uso

        #calculando as horas que o usuario deseja usar
        horas_usadas = hora_final - hora_atual

        #verficando se a quantidade de horas que o usuario deseja usar é equivalente ao que ele pode usar
        if horas_usadas <=4 and horas_usadas > 0:

            #verificando se o horario esta dentro do horario comercial
            if  hora_atual >= 9 and hora_final <=18:
                print("Acesso liberado ")
            else:
                print("Acesso negado - horário fora do horario comercial")

        else:
            print("Acesso negado - intervalo muito longo para seu tipo de usuario")
    else:
        print("Acesso negado - VIsitantes não são autorizados a usar esse site durante o final de semana")
