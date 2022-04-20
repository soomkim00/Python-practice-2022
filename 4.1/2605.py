N = int(input())
line_list = []
num_list = list(map(int, input().split()))

for i in range(N):
    line_list.insert(num_list[i], i+1)

line_list.reverse()

for j in range(N):
    print(line_list[j], end=' ')
