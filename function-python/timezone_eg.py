import datetime 
import pytz

utc = pytz.utc
now = datetime.now(utc)

india = pytz.timezone('Asia/Kolkata')
print(now.astimezone(india))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat )   
print(dt_mtn.strftime('%B %d, %Y'))
dt_mtn = datetime.datetime.now()
dt_east = dt_mtn.astimezone(pytz.timezone('US/Easter'))
print(dt_mtn)

for tz in pytz.all_timezones:
    pytz(tz)
#Converts time → India timezone

#Why we use it
# Handle global apps (different countries)
# Avoid wrong time calculations
# Important in backend / APIs


#In Python 3.9+ use:

#from zoneinfo import ZoneInfo