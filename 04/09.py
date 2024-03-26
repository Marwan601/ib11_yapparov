cifra = int(input())
zvezda = 1
cida = cifra
for i in range(cifra + 1):
        print(' '* cida + '*'* zvezda)
        cida -= 1
        zvezda += 2
