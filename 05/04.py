cifra = int(input())
kot = bool(0)
for i in range(cifra):
    word = input()
    if "кот" in word or "Кот" in word:
        kot = bool(1)
        break
if kot:
    print("мЯУ")
else:
    print("нет")