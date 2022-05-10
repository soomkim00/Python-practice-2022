t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    v = [0 for j in range(n)]
    v[m] = 1
    count = 0
    while True:
        if s[0] == max(s):
            count += 1
            if v[0] == 1:
                print(count)
                break
            else:
                v.append(0)
                s.append(0)
        else:
            s.append(s[0])
            del s[0]
            v.append(v[0])
            del v[0]
