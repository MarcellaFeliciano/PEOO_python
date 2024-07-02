#script que faz a contagem regressiva de um foguete
print("-"*30)
print("Contagemm regressiva!")
from time import sleep
cont = 10
while cont!=0:
    print(f"{cont} ", end='', flush=True)
    sleep(0.5)
    cont-=1
print("FOGO!")
print("-"*30)
