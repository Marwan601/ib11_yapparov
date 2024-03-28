pravda = False
cifra = int(input())
for i in range(cifra+1):
    zapros = input()
    if zapros == 'С кем война?':
        if pravda:
            print("Океания")
        else:
            print("Eвразия")
    elif zapros == "С кем мир?":
        if pravda:
            print("Евразия")
        else:
            print("Океания")
    elif zapros == "Меняем":
        if pravda:
            pravda = False
        else:
            pravda = True
