A = list(input())
B = list(input())
i = 0

while i < len(A):
    if A[i] in B:
        B.remove(A[i])
        A.remove(A[i])
        i -= 1
    i += 1

print(len(A) + len(B))
