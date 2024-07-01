
try:
    import matematica as math

except ModuleNotFoundError as erro1:
    print(f"Erro: {erro1}")
    print(f"Classe: {type(erro1)}")
# ModuleNotFoundError: No module named 'matematica'
try:
    print(math.sen(30))

except NameError as erro2:
    print(f"Erro: {erro2}")
    print(f"Classe: {type(erro2)}")


