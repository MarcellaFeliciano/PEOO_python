#script que solicita 3 estaturas (alturas) e informa a maior
print("-="*25)
alt_1 = float(input("- Primeira altura: "))
alt_2 = float(input("- Segunda altura: "))
alt_3 = float(input("- Terceira altura: "))

if alt_1 == alt_2 or alt_1 == alt_3 or alt_2==alt_3:
    print(f"Há, pelo menos, 2 pessoas com a mesma estatura!")
elif alt_1>alt_2 and alt_1>alt_3:
    print(f" A maior altura é {alt_1}")
elif alt_2>alt_1 and alt_2>alt_3:
    print(f" A maior altura é {alt_2}")
elif alt_3>alt_1 and alt_3>alt_2:
    print(f" A maior altura é {alt_3}")

print("-="*25)
