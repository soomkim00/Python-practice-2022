S = list(input())
al = [0]*26
pos = [-1]*26
n = 97

for i in range(26):
    al[i] = n
    n += 1

k = 0
for i in S:
    for j in range(26):
        if ord(S[k]) == al[j] and pos[j] == -1:
            pos[j] = k
    k += 1

print(*pos)
