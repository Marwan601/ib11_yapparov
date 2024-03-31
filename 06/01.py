sol = set()
ky = set()
badguy = 0
kise = 0
while badguy != "":
    badguy = input()
    if badguy != "":
        sol.add(badguy)
    else:
        badguy = ""
while kise != "":
    kise = input()
    if kise != "":
        ky.add(kise)
    else:
        kise = ""
guilty = sol & ky
if guilty != set():
    print(*guilty, sep = "\n")
else:
    print("EMPTY")

