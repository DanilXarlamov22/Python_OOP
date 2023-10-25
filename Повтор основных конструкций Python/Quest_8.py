from datetime import date
import calendar

year = int(input())
month = int(input())
count = 0
for k in range(1, calendar.monthrange(year, month)[1] + 1):
    if calendar.weekday(year, month, k) == 3:
        count += 1
        if count == 4:
            print(date(year, month, k).strftime("%d.%m.%Y"))