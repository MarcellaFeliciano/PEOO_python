while True:
    try:
        nome = input('informe um nome (que não seja rk): ')
        if nome == 'rk':
            raise Exception('RK não pode ser o nome pq é Internacional') 
            # a classe de errro Exception abrange todos os erros!
            
            # gera um erro! logo, como irá da erro ela irá cair no 'except' onde o Exception descobreto/levantado 
            # será atribuido a variavel erro!  onde irá sera mostrado na tela que ocorreu um erro do tipo tal
        print(nome)
    except Exception as erro_customizavel:
        print(f"Ocorreu um erro do tipo: {erro_customizavel}")
    else: 
        break

print(nome)