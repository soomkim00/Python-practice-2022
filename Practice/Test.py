def fibo(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        next = f1 + f2
        f1 = f2
        f2 = next
    return f1


a = int(input())
print(fibo(a))