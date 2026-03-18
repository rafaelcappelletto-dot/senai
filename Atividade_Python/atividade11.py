estoque ={}
total =0
#boas vindas
print("Bem vindo ao sistema de gestão de estoque desenvovido por Rafael Cappelletto")

while True:
    #pedindo a opção que o usuario deseja
    operacao = (input("\nDeseja registrar uma entrada ou saida? (Digite 'entrada', 'saida' ou 'sair'): ")).lower() #faz todas as letras ficarem minusculas

    #verificando se a opção escolhida é valida
    if operacao not in ["entrada","saida","sair"]: 
        print("\n Operação invalida.")
        continue#volta do começo instantaneamente
    
    if operacao == "sair":
        break#para o while

    #pedindo o nome e a quantidade do produto que o usuario deseja alterar
    produto = input("\nNome do produto: ").strip()#se for quase a mesma palavra ele vai colocar na mesma informação
    qtd = int(input("Quantidade do produto: "))

    if operacao == "entrada":
        #adicionando a quantidade ao produto dentro do dicionario
        estoque[produto] = estoque.get(produto, 0) + qtd
        #somando no total de produtos
        total += qtd
      

    elif operacao =="saida":
        #Verificando se o produto tem a quantidade maior ou igual do que eu desejo tirar ou se ele existe
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
            #Diminuindo o total de pordutos
            total -= qtd
        
        else:
            print("\nErro: Produto inexistente ou estoque insuficiente")
    
#desenhando o estoque final
print("\n--- Estoque Final ---")

for p,q in estoque.items():
    print(f"{p}:{q}")
       
#escrevendo o total de produtos do estoque
print(f"Total de produtos em estoque:{total}")
      

