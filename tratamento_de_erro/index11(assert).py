nome = input("Digite um Nome:")
"""if nome == 'Marcela':
    raise NameError('Nome Proibido')
    """
assert nome != 'Marcella', 'Nome Proibido!'
 # simplicado, onde essa é assertiva - AssetionError - se o nome for diferetnte de
 # Marcella está correto, caso contraio a mensagem de errro é informada!


print(nome)