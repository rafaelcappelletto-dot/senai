import time
segundos = 10

for i in range(segundos):
    print(f"Tempo restante: {segundos} segundos")
    segundos -=1
    time.sleep(1)

print("resfriamento concluido")
