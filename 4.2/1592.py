N, M, L = map(int, input().split())
yo = [0]*N
yo[0] = 1
ball = 0
count = 0

while max(yo) < M:
    if yo[ball] % 2 == 1:
        ball = (ball + L) % N
        yo[ball] += 1
        count += 1
    else:
        ball = (ball + N - L) % N
        yo[ball] += 1
        count += 1

print(count)
