import pickle

material = ['caderno','lapis']

arq = open('marcella.bin','wb')
pickle.dump(material,arq)

arq.close()

