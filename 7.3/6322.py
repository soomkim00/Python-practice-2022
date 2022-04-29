import math as m
i = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if c != -1 and max(a, b) >= c:
        print('Triangle #{}'.format(i))
        print("Impossible.")
    elif c == -1:
        print('Triangle #{}'.format(i))
        print('c = %.3f' % m.sqrt(a**2 + b**2))
    elif b == -1:
        print('Triangle #{}'.format(i))
        print('b = %.3f' % m.sqrt(c**2 - a**2))
    elif a == -1:
        print('Triangle #{}'.format(i))
        print('a = %.3f' % m.sqrt(c**2 - b**2))
    print()
    i += 1
