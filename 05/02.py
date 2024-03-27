cifra = int(input())
kot = bool(0)
for i in range(cifra):
    word = input()
    if "кот" in word:
        kot = bool(1)
if kot:
    print("мЯУ")
else:
    print("нет")
