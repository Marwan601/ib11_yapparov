true = ""
pasword = input()
pasword1 = input()
while true != "ok":
    if len(pasword) < 8:
        print("короткий")
        pasword = input()
        pasword1 = input()
    elif "123" in pasword:
        print("слишком простой")
        pasword = input()
        pasword1 = input()
    elif pasword != pasword1:
        print("различаются")
        pasword = input()
        pasword1 = input()
    else:
        true = "ok"
        print(true)