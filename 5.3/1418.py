def sejun(n, k):
    s = [0]*(n + 1)
    for i in range(2, n + 1):
        if s[i] == 0:
            for j in range(i, n + 1, i):
                if j % i == 0:
                    s[j] = max(s[j], i)
    total = 0
    for i in s:
        if i <= k:
            total += 1
    print(total - 1)


N = int(input())
K = int(input())
sejun(N, K)
