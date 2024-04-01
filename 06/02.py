sol = set()
ky = set()
cifra = int(input())
for i in range(cifra):
    word = input()
    sol.add(word)
word = input()
ky.add(word)
badguy = sol & ky
if badguy != ky:
    print("ok")
else:
    print("try another")