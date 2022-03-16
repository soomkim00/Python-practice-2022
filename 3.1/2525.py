h, m = map(int, input().split())
c = int(input())
h2 = h+(m+c)//60
m2 = (m+c)%60
if h2 >= 24 :
    h2 = h2 - 24
print(h2, m2)