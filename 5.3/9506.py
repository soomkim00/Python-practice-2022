def is_perfect_num(n):
    div = []
    until = int(n**(1/2))
    total = 1
    for i in range(2, until + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    div.sort()
    for j in div:
        total += j
    if total == n:
        print(n, "= 1", end=' ')
        for k in div:
            print("+", k, end=' ')
        print("")
    else:
        print(n, "is NOT perfect.")


while True:
    N = int(input())
    if N == -1:
        break
    is_perfect_num(N)
