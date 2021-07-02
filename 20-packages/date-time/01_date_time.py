import datetime

now = datetime.datetime.now()
print(now)
print("year",now.year)
print("month",now.month)
print("day",now.day)

if now.day == 25 and now.month == 12:
    print("christmas")
else:
    print("not christmas")