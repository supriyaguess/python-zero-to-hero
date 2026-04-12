import datetime
import timezone #pytz is a Python library used to work with time zones
 
d = datetime.date(2026,11,6)
print(d)

tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(tday.weekday())
# print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
# print(tday-tdelta)
# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2026,9,24)

till_bday = bday- tday
print(till_bday)
print(till_bday.total_seconds())

t = datetime.time(9,30,45,10000)
print(t.hour)

dat = datetime.datetime(2026,7,26,12,30,45,100000)
print(dat.time())
#print(dat.years())


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)