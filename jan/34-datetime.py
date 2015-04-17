# 34-datetime.py

from datetime import datetime, date, timedelta

now = datetime.now()

print(now)
print(type(now))
print('Day', now.day)
print('Year', now.year)
print('Month', now.month)
print('Hour', now.hour)
print('Minutes', now.minute)
print('Seconds', now.second)


today = date.today()
print(today)

for day in range(1, 10):
    future = today + timedelta(days=day)
    print(future)
