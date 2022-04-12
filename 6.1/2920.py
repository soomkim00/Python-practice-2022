def check(s):
    if s == sorted(s):
        print("ascending")
    elif s == sorted(s, reverse=True):
        print("descending")
    else:
        print("mixed")


S = list(map(int, input().split()))
check(S)
