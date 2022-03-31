card = list(range(1, 21))

for i in range(10):
    a, b = map(int, input().split())
    temp = card[a-1:b]
    temp = reversed(temp)
    card[a-1:b] = temp

print(*card)