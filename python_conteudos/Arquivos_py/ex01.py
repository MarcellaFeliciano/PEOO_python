# arquivos em python
# open - manipula(interagi) - fecha
# - arquivos text
# mode -> 'r' (read) / 'w' (write)

arq = open('exemplo.txt','r') #r de leitura (read)

print(type(arq)) 

conteudo = arq.read()
print(conteudo)
print(type(conteudo)) 

conteudo = arq.readlines()
print(type(conteudo))
print(conteudo)
for i in range(len(conteudo)):
    print(f"Linha - {conteudo[i]}")
arq.close()