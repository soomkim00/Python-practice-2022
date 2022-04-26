import calendar
import calendar as cl

daylist = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
a, b = map(int, input().split())
day = cl.weekday(2007, a, b)
print(daylist[day])
