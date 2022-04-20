a_list = []

for i in range(9):
    a_list.append(int(input()))

Max_num = max(a_list)
print(Max_num)
print(a_list.index(Max_num)+1)
