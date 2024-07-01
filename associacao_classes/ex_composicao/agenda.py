from classes_agenda import Amigo

amigo1 = Amigo('Zé')
amigo1.inserir_telefone(84,'99999-9999')
amigo1.inserir_telefone(84,'88888-8888')
amigo1.inserir_telefone(84,'77777-7777')

amigo2 = Amigo('Chico')
amigo2.inserir_telefone(84,'11111-1111')
amigo2.inserir_telefone(84,'22222-2222')

print(amigo1.nome)
amigo1.listar_telefones()