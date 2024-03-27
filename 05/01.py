a = int(input())
b = int(input())
while not a > b:
    a = int(input())
    b = int(input())
for i in range(b,a + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
        three = bool(1)
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)