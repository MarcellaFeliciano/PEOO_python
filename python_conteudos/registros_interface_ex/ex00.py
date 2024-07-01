import pickle


# codificação - desserelização 


# pickle.dump
# pickle.load

alunos = {'Joao':5, "Maria":8}
arq = open('resutado.txt','wb')
pickle.dump(alunos,arq) # arquivo para gravar q gera o arquivo com dump

arq.close()