#script que solicita notas do aluno e informa sua situaçao
print("-="*20)
print(F'{"S I T U A Ç Ã O   E S C O L A R":^40}')
print("-"*40)
nota_1 = float(input("- Primeira nota: "))
nota_2 = float(input("- Segunda nota: "))
m = (nota_1+nota_2)/2
print(" ~ ~"*10)
if m>=7:
    print(f" Aprovado! Média {m:.1f}")
elif m<4:
    print(f" Reprovado! Média {m:.1f}")
elif m>=4 and m<7:
    print(" Em recuperação!")
    af = float(input("- Nota da avaliação final: "))
    m_final =(m + af)/2
    print(f" A média final do aluno foi: {m_final:.1f}")
print("-="*20)