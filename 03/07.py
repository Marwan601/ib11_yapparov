user = 1
a = 1
one = 0
two = 1001
while user != "=":
    a = (one + two) // 2
    print(a)
    print('это ваше число?')
    user = input()
    if user == ">":
        one = a
    elif user == "<":
        two = a
print("ваше число:", a)