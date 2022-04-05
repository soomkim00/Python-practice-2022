def com_2(a, b):
    for n in range(1, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            print(n)


def com_3(c, d, e):
    for n in range(1, min(c, d, e) + 1):
        if c % n == 0 and d % n == 0 and e % n == 0:
            print(n)


N = int(input())
if N == 2:
    f, g = map(int, input().split())
    com_2(f, g)
else:
    h, i, j = map(int, input().split())
    com_3(h, i, j)
