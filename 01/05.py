one = input()
two = input()
three = input()
if one == "раз" or one == "1" and two == "два" or two == "2" and three == "три" or three == "3":
    print("ГОРИ")
elif one == "один" and not two == "2" and not three == "3":
    print("ГОРИ")
else:
    print("НЕ ГОРИ")  # не работает
