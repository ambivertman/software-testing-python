import datetime

now = datetime.date.today()
for i in range(1,366):
    newday = now + datetime.timedelta(i)
    if newday.weekday() == 0:
        print(newday.strftime("%Y-%m-%d"))