import sys

N = int(input())
q = []

while True:
    num = int(sys.stdin.readline().rstrip())
    if num > 0 and len(q) < N:
        q.append(num)
    elif num == 0:
        q.pop(0)
    elif num == -1:
        break

if len(q) == 0:
    print('empty')
else:
    print(*q)
