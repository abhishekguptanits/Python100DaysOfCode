import datetime as dt

current_date_time = dt.datetime.now()
current_year = current_date_time.year
current_month = current_date_time.month
day_of_week = current_date_time.weekday()   # Monday - 0, Tuesday - 1

date_of_birth = dt.datetime(year=1995, month=12, day=25, hour=14)

print(date_of_birth)