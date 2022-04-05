def find_factor(n, k):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        if count == k:
            return i
    if count < k:
        return 0


n, k = map(int, input().split())
print(find_factor(n, k))