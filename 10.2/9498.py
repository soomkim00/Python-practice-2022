n = input()
A = lambda x: 100 >= x >= 90, n
B = lambda x: 90 > x >= 80, n
C = lambda x: 80 > x >= 70, n
D = lambda x: 70 > x >= 60, n
E = lambda x: 60 > x, n
grade = (A, B, C, D, E)

print(grade)


# print(map(lambda x: 'A' if x >= 90 else 'B' if 90 > x >= 80 else 'C' if 80 > x >= 70 else 'D'
# if 70 > x >= 60 else 'E', input()))
