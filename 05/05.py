kot = bool(0)
for i in range(100):
    word = input()
    if word == "СТОП":
        break
    elif "кот" in word or "Кот" in word:
        kot = bool(1)
        nomer = i
        break
if kot:
    print(nomer)
else:
    print(-1)