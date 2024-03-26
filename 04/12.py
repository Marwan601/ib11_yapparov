cifra = int(input())
sol = 0
for i in range(cifra):
    nature = int(input())
    if i == 0:
        sol += nature
    elif i % 2 != 0:
        sol -= nature
    else:
        sol += nature
print(sol)