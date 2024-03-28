koti = 0
kot = False
cifra = 0
slova = 1
while slova != "СТОП":
   slova = input()
   if kot == False:
      cifra += 1;
   if "кот" in slova:
      kot = True
      koti += 1
print(koti, cifra)