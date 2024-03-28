cifra = False
sol = 0
nomer = 0
summa = 1
while summa != 0:
    summa = input()
    summa += sol
    nomer += 1
    if sol > 10:
        print(nomer)
        break
while summa != 0:
    summa = input()
    sol += summa
    nomer += 1

