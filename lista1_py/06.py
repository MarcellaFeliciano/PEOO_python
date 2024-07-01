#script do calendario de abril/2023
n=0
print("-"*35)
print(" abril 2023")
print("-"*35)
print(" dom  seg  ter  qua  qui  sex  sab")
for d in range(-5,37):
    if n/7 == 1:
        print()
        n=0
    if d <= 0 or d >30:
        print("     ", end='')
        n+=1
    else:
        print(f" {d:<4}", end='')
        n+=1
print()
print("-"*35)
