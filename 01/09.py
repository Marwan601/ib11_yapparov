login = input("введите логин:")
pochta = input("введите почту:")
if "@" not in login and "@" in pochta:
    print("OK")
elif  "@" in login and "@" not in pochta:
    print("Некорректный логин", "\n", "некорректная почта", sep="")
elif "@" not in login and "@" not in pochta:
    print("некорректная почта")
elif "@" in login and "@" in pochta:
    print("Некорректный логин")
