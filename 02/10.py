a = float(input("первое число:"))
b = float(input("второе число:"))
c = input("операция:")
if c == "*":
    print(a * b)
elif c == "/" and b == 0:
    print(888888)
elif c == "/":
    print(a / b)
elif c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
else:
    print(888888)