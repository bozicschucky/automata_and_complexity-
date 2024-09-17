def no_consecutive_ones(s):
    start = "s"

    for i in range(len(s)):
        if start == "s" and s[i] == "1":
            start = "1"
        elif start == "1" and s[i] == "1":
            return False
        elif s[i] == "0":
            start = "s"

    return True


print(no_consecutive_ones("1010"))  # True
print(no_consecutive_ones("110"))  # False
