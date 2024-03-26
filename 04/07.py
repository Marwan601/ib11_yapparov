tik = 0
cifra = int(input())
for i in range(1,cifra+1):
    if cifra % i == 0:
        tik = tik + 1
        print(i,end=" ")
if tik > 2:
    print("\n""нет")
else:
    print("\n""простое")



