from datetime import datetime, date, time


d = date(2005, 7, 14)
t = time(12, 30)
print(datetime.combine(d, t))