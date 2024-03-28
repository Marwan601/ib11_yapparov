kot = False
cifra = int(input())
for i in range(cifra):
    word = input()
    if "кот" in word or "Кот" in word:
        kot = True
    if "пёс" in word or "Пёс" in word:
        kot = False
if kot:
    print("МЯУ")
else:
    print("нет")