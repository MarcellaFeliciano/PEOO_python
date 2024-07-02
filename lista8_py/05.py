#  programa em Python que pede que o usuário informe sua data de nascimento (dia, mês e ano) e, utilizando funções da biblioteca datetime (para saber a data em que o programa está sendo executado) calcule e informe quantos anos o usuário tem.

from datetime import date

def main():
    print("-"*40)
    print(f'{"D A T A":^40}')
    print("-"*40)
    print("Informe sua data de nascimento:")
    data = input("[dd/mm/aaaa] = ")
    mostrar(data)
    print("-"*40)


def mostrar(data):
    dt = data.split('/')
    dia = int(dt[0])
    mes = int(dt[1])
    ano = int(dt[2])

    data_atual = date.today()
    data_atual = str(data_atual)
    data_atual = data_atual.split('-')

    dia_atual = int(data_atual[2])
    mes_atual = int(data_atual[1])
    ano_atual = int(data_atual[0])

    anos = 0
    meses = 0
    dias = 0

    if dia_atual >= dia:
        dias = dia_atual - dia
    else:
        cont = dia
        while cont < 31:
            cont += 1
            dias += 1
        dias += dia_atual
        meses -= 1
        if dias > 31:
            dias = dias - 31

    
    if mes_atual >= mes:
        meses = mes_atual - mes
        anos = ano_atual - ano
        if dia_atual < dia:
            meses -= 1
    else:
        cont = mes
        while cont < 12:
            meses += 1
            cont += 1
        meses += mes_atual
        anos = (ano_atual - ano) - 1

    print("_"*40)
    print(f'{"Sua Idade":^40}')
    print(f'~> {anos} anos, {meses} meses e {dias} dias!')
    

if __name__ == '__main__': # chamada da funcao principal
    main()