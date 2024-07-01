import pickle

arq = open('marcella.bin','rb')
meu_material = pickle.load(arq)

print(meu_material[0])