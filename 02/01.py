one = input()
two = input()
if one == "Тула" and two == "Пенза":
    print("нет")
elif one == "Пенза" and two == "Тула":
    print("нет")
elif one == two:
    print("нет")
else:
    print("ДА")