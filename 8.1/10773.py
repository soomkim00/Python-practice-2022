k = int(input())
st = []

for _ in range(k):
    n = int(input())
    if n == 0:
        del st[-1]
    else:
        st.append(n)

print(sum(st))
