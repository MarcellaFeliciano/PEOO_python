senha = ''
while True:
    try:
        senha = input('Digite uma senha: ')
        if len(senha) < 8:
            raise Exception('Senha menor que 8 caracteres')
        elif senha == 'internacional':
            raise Exception('Senha não pode ser internacional!')
        else:
            break
    except Exception as erro:
        print('Erro')

print(f'Senha criada com sucesso: {senha}')