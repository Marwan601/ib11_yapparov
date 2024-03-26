kol = int(input("количество человек:"))
iq = 0
for i in range(kol):
    cifra = int(input())
    iq += cifra
    if i == 0:
        print("0")
    elif iq / (i + 1) < cifra:
        print(">")
    elif iq / (i + 1) > cifra:
        print('<')
    else:
        print(0)