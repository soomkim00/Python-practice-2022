A = int(input())
B = int(input())
C = int(input())
n = A*B*C
n_list = list(str(n))
for i in range(10):
    print(n_list.count(str(i)))