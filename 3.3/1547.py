M = int(input())
A = [1, 0, 0]

for i in range(M):
    a, b = map(int, input().split())
    t = A[a-1]
    A[a-1] = A[b-1]
    A[b-1] = t

for j in range(3):
    if A[j] == 1:
        print(j+1)