
# erro na importação da biblioteca 
# ModuleNotFoundError: No module named 'matematica'
try:
    import matematica as math

except ModuleNotFoundError as erro1:
    print("-"*35)
    print(f"Erro: {erro1}")
    print(f"Classe: {type(erro1)}")

# erro no uso da função que não esta importada
# NameError: name 'math' is not defined
try:
    print(math.sen(30))

except NameError as erro2:
    print("-"*35)
    print(f"Erro: {erro2}")
    print(f"Classe: {type(erro2)}")

