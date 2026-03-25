ciclos = int(input("Digite o numero de ciclos: "))
pressao = int(input("Pressão: "))
temperatura = int(input("temperatura: "))

if ciclos < 200:
    reducao = 0.00  

elif ciclos >=200 and ciclos < 1000:
    reducao = 0.05  
 
elif ciclos >= 1000 and ciclos < 1999:
    reducao = 0.10  
  
elif ciclos >= 2000:
    reducao = 0.15 
   
else:
    print("Valor invalido")  
    
pressão = pressao -((pressao * reducao) / 100)


