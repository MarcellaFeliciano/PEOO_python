#script que calcula o tempo para percorrer uma viagem
print('-='*30)
velocidade = float(input("- Digite a velocidade (km/h) media do carro: "))
distancia = float(input("- Digite a distancia (km) que será percorrida: "))
tempo = distancia/velocidade
print(f" A viagem levará {tempo}h/min")
print('-='*30)