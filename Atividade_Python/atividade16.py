

print("Boas-Vindas Rafael")

for i in range(5):
    leitura = float(input("Digite o valor da leitura: "))
    horas = float(input(f"Digite o número de horas que o sensor{i+1} foi usado: "))

    if horas < 200:
        ajuste = 0
    elif horas >= 200 and horas < 1000:
        ajuste = 5
    elif horas >= 1000 and horas < 2000:
        ajuste = 10
    elif horas >= 2000:
        ajuste = 15
    else:
        print("Valor invalido")

    print("Horas:",horas)
    print("Leitura bruta: ",leitura)

    leitura = leitura -((leitura * ajuste) / 100)

    print("Leitura calibrada: ",leitura)

   