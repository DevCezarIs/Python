import datetime

d = datetime.datetime(2024, 6, 30, 15, 45, 00)
print(d)

d = d + datetime.timedelta(weeks=1)
print(d)