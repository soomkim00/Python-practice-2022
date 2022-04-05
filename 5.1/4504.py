def is_multiple(a, b):
    if a > b:
        return 1
    elif b % a != 0:
        return 1
    else:
        return 0


n = int(input())
while True:
    m = int(input())
    if m == 0:
        break
    print(m, "is ", end='')
    if is_multiple(n, m):
        print("NOT ", end='')
    print("a multiple of", n, end='')
    print(".")