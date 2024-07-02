# Programa que contenha uma função que recebe uma string e devolve uma outra string de mesmo tamanho alterando cada vogal por um símbolo diferente 

def main():
    while True: 
        print('-='*30)
        mens = input("Digite uma mensagem para ser codificada: ").lower()
        mens_cod = codificador(mens)
        print(f"- Mensagem codificada: {mens_cod}")
        condicao = input("Deseja continuar? [S/N] ").upper().strip()
        if condicao == 'N':
            print("-"*60)
            break
        


def codificador(mensagem):
    mens_cod = ''
    for i in mensagem:
        if i == 'a':
            mens_cod +='$'
        elif i == 'e':
           mens_cod +='&'
        elif i == 'i':
            mens_cod +='!'
        elif i == 'o':
            mens_cod +='%'
        elif i ==  'u':
            mens_cod +='?'
        else:
            mens_cod+=i
    return mens_cod


if __name__ == '__main__': # chamada da funcao principal
    main()