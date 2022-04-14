N = int(input())
num = list(input())
total = 0
for _ in range(N):
    total += int(num.pop())
print(total)
