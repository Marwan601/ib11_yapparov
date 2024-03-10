music = input("вы любите музыку:")
art = input("вы любите искусво:")
if "да" in music and "нет" not in music and "да" in art and "нет" not in art:
    print("вы творческая личность")
elif "да" in music and "нет" not in music and "нет" in art and "да" not in art:
    print("вы меломан")
elif "нет" in music and "да" not in music and "нет" in art and "да" not in art:
    print("вы интересная личность")
elif "нет" in music and "да" not in music and "да" in art and "нет" not in art:
    print("вы неординарная личность")
else:
    print("ошибка не правильный ответ")
