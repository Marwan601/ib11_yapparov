ops = 1
for i in range(6):
    cifr = int(input())
    if cifr != 0:
        ops = cifr * ops
    elif cifr == 0:
        ops = 1 * ops
else:
    print(ops)