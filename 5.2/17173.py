def mul(n, k):
    mulsum = 0
    for i in range(k[0], n + 1):
        for ki in k:
            if i % ki == 0:
                mulsum += i
                break
    return mulsum


N, M = map(int, input().split())
K = list(map(int, input().split()))

print(mul(N, K))
