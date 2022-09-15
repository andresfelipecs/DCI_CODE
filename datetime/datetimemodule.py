from datetime import datetime, date

# get current date and time
print(datetime.today())

# get current date
print(date.today())

# convert string to date iso with datetime
date_as_string = '2022-01-26'
print(date.fromisoformat(date_as_string))

# print the submodules
print(dir(datetime))

# date time objects 
# date time object with time

date_1 = datetime(2022, 1, 26, 10, 30, 59)
date_1 = datetime(year= 2022, month=1, day=26, hour=10, minute=30, second=59)
print(date_1)

# date time object without time 
date_2 = date(year=2022, month=2, day=12)
date_2 = date(2022, 2, 12)
print(date_2)

# datetime.strptime(usa_meeting, "%B %d, %Y")
# strptime() Parse a string into a datetime object given a corresponding format

date = 'January 1, 2005'
p = datetime.strptime(date, "%B %d, %Y")
print(p, type(p))
# prints the time in format hour/minute/seconds
# strftime() Convert object to a string according to a given format
f = datetime.now().strftime('%H:%M:%S')
print(f, type(f))



