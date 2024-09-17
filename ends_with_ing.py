def ends_with_ing(word):
    start = "start"

    for i in range(len(word)):
        if (start == "start" and word[i] == "i"):
            start = "i"

        elif (start == "i" and word[i] == "n"):
            start = "n"

        elif (start == "n" and word[i] == "g"):
            start = "g"
        else:
            start = "start"

    return start == "g"


print(ends_with_ing("running"))  # True
print(ends_with_ing("run"))  # False
print(ends_with_ing("sing"))  # False
