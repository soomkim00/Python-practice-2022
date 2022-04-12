while True:
    try:
        sen = input()
        lo, up, num, bl = 0, 0, 0, 0
        for i in sen:
            if i.islower():
                lo += 1
            elif i.isupper():
                up += 1
            elif i.isdigit():
                num += 1
            elif i.isspace():
                bl += 1
        print(lo, up, num, bl)
    except EOFError:
        break
