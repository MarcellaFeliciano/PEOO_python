import warnings

def somapositivos(a,b):
   if a < 0 or b < 0:
        #raise ValueError('Valor Negativo Informado')
        warnings.warn('Mensagem  de erro')
        #warnings.simplefilter('default') UserWarning) # alerta e continua
        return a+b


print(somapositivos(4,-3))
