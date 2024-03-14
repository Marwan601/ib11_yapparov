pawpas = input("придумайте пароль:")
cifra = len(pawpas)
if cifra < 8:
    print("короткий")
    exit()
else:
    pov = input("повторите пароль")
if pov == pawpas:
    print("ok")
else:
    print("различаются")