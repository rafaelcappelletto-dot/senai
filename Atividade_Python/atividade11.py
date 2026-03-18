estoque ={}
total =0
print("Bem vindo ao sistema de gestão de estoque desenvovido por Rafael Cappelletto")

while True:

    operacao = (input("\nDeseja registrar uma entrada ou saida? (Digite 'entrada', 'saida' ou 'sair'): ")).lower() #faz todas as letras ficarem minusculas

    
    if operacao not in ["entrada","saida","sair"]: #se nao for entrada , saida ou sair
        print("\n Operação invalida.")
        continue#volta do começo insta

    if operacao == "sair":
        break#para o while

    produto = input("\nNome do produto: ").strip()#se for quase a mesma palavra ele vai colocar na mesma informação
    qtd = int(input("Quantidade do produto: "))

    if operacao == "entrada":
        estoque[produto] = estoque.get(produto, 0) + qtd
        total += qtd
        

    elif operacao =="saida":
        if estoque.get(produto, 0) >= qtd:# se for maior que a quantidade que desejo remover e se o produto existe
            estoque[produto] -= qtd
            total -= qtd
            
        else:
            print("\nErro: Produto inexistente ou estoque insuficiente")
    
#desenhando o estoque final
print("\n--- Estoque Final ---")

for p,q in estoque.items():
    print(f"{p}:{q}")
       
print(f"Total de produtos em estoque:{total}")
      

