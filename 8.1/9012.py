import sys
T = int(input())

for _ in range(T):
    stk = []
    st = sys.stdin.readline().strip()
    for s in st:
        if s == '(':
            stk.apped(s)
        elif s == ')':
            if stk:
                stk.pop()
            else:
                print('NO')
    else:
        if not stk:
            print("YES")
        else:
            print("NO")
