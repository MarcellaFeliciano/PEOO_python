# Faça uma função que recebe como parâmetro uma data (no formato DD/MM) e informa a data por extenso. 


def main():
    print("-="*20)
    print(f'{"D A T A":^40}')
    print("-="*20)
    data = input("Informa uma data: [dd/mm] ")
    mostrar_data(data)
    print("-="*20)


def mostrar_data(data):

    dias = ['um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte','vinte um','vinte e dois','vinte e três','vinte e quatro','vinte e cinco','vinte e seis','vinte e sete','vinte e oito','vinte e nove','trinta','trinta e um']
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro',]
    dt = data.split('/')
    dia = dt[0]
    mes = dt[1]
    novo_mes = ''
    novo_dia = ''

    for d in range(1,31+1):
        if d < 10:
            if '0'+str(d) == dia:
                novo_dia = dias[d-1]
        else:
            if str(d) == dia:
                novo_dia = dias[d-1]

    for m in range(1,13):
        if m < 10:
            if '0'+str(m) == mes:
                novo_mes = meses[m-1]
        else:
            if str(m) == mes:
                novo_mes = meses[m-1]

    print(f"Data por extenso: {novo_dia.capitalize()} de {novo_mes}")


if __name__ == '__main__':
    main()