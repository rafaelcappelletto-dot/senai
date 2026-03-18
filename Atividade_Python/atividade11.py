estoque ={}

print("Bem vindo ao sistema de gestão de estoque desenvovido por Rafael Cappelletto")

while True:

    operacao = (input("Deseja registrar uma entrada ou saida?(Digite 'entrada', 'saida' ou 'sair'): ")).lower() #faz todas as letras ficarem minusculas

    
    if operacao not in ["entrada","saida","sair"]: #se nao for entrada , saida ou sair
        print("Operação invalida.")
        continue

    if operacao == "sair":
        break#para o while
    produto = input("Nome do produto: ")

   

   
       
      

