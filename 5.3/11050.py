def bino(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))


def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


N, K = map(int, input().split())
print(bino(N, K))
