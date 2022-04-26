import datetime as dt
today = dt.date.today()
gap = dt.timedelta(hours=9)
utc = today - gap
print(utc.year)
print(utc.month)
print(utc.day)
