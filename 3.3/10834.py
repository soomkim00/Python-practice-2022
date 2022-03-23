M = int(input())
Dir = 0
Turn = 1

for i in range(M):
    a, b, d = map(int, input().split())
    if d == 1:
        Dir += 1
    Turn = Turn * b / a

print((Dir % 2), int(Turn))