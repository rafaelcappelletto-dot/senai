
soma = 0

for i in range(5):
    salarios = float(input(f"Funcionário {i+1}, escreva o seu salário: "))

    soma += salarios

media = soma/5
print(f"A média dos salários é {media}")