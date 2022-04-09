def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B), gcd(A, B))
