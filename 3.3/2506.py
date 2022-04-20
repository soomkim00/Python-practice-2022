N = int(input())
Ans = list(map(int, input().split()))
score, add = 0, 0
for i in range(N):
    if Ans[i] == 1:
        add += 1
        score += add
    else:
        add = 0
print(score)
