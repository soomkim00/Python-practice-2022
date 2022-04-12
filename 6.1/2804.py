A, B = list(input().split())
apos, bpos = -1, -1

for i in range(len(A)):
    if apos != -1:
        break
    for j in range(len(B)):
        if A[i] == B[j]:
            apos, bpos = i, j
            break

for i in range(len(B)):
    if i == bpos:
        for a in A:
            print(a, end='')
        print()
    else:
        for a in range(apos):
            print('.', end='')
        print(B[i], end='')
        for a in range(len(A) - apos - 1):
            print('.', end='')
        print()
