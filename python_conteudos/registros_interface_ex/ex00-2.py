import pickle

arq = open('resutado.txt','rb')

arquivoDesserializado = pickle.load(arq)

print(arquivoDesserializado)
arq.close()

arq = open('resutado.txt','r')


arquivoAberto = arq.read()
print(arquivoAberto)

arq.close()