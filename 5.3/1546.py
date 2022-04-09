def aver(n, s):
    s.sort()
    m = s[-1]
    for i in range(len(s)):
        s[i] = s[i] / m * 100
    total = 0
    for i in range(len(s)):
        total += s[i]
    return total / len(s)


N = int(input())
S = list(map(int, input().split()))
print(aver(N, S))
