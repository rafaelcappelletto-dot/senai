import time

num =int(input("Digite o numero para ver a tabuada: "))

for i in range(10):
    print(f"{num} X {i+1} = {num*(i+1)}")
    time.sleep(1)


