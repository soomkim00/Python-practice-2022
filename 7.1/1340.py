mon, d, y, t = input().split()
d = int(d[:-1])
y = int(y)
h, m = map(int, t.split(':'))
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    day[1] += 1
total = sum(day) * 24 * 60
last = month.index(mon)
current = (sum(day[:last]) + d - 1) * 24 * 60 + h * 60 + m
print(current/total * 100)
