import datetime as dt
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

Dday = dt.date(y2, m2, d2)
today = dt.date(y1, m1, d1)
gap = str(Dday - today).split(" ")[0]
if int(gap) >= 365243:
    print("gg")
else:
    print(f"D-{gap}")
