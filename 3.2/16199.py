Y1, M1, D1 = map(int, input().split())
Y2, M2, D2 = map(int, input().split())

O1 = Y2 - Y1
if M2 - M1 < 0 or (M2 == M1 and D2 - D1 < 0):
    O1 = O1 - 1

O2 = Y2 - Y1 + 1

O3 = O2 - 1

print(O1)
print(O2)
print(O3)