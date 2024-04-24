from datetime import datetime, timedelta
"""
datetime.datetime: This class represents a specific date and time.
It includes both the date and time components, down to the microsecond.

You can create a datetime object using the constructor 
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0).
"""

dt = datetime(2024, 4, 23, 12, 30, 45)
print(dt)
print(datetime.year)
print(datetime.month)
print(datetime.day)
print(datetime.hour)
print(datetime.minute)
print(datetime.second)
print(datetime.microsecond)

"""
The datetime.date class represents only the date component without the time. 
The datetime.datetime extends this functionality to include the time as well.
"""
dt1 = datetime(2024, 4, 23, 12, 0, 0)
dt2 = datetime(2024, 4, 25, 10, 30, 0)

diff = dt2 - dt1
print(diff)

"""
attributes in timedelta:
days: number of days
seconds: number of seconds
microseconds: number of microseconds
minutes: number of minutes
hours: number of hours
weeks: number of weeks
"""
d1 = dt1 + timedelta(days=5)
print(d1)

d2 = dt1 - timedelta(days=5)
print(d2)

d3 = dt1 + timedelta(days=2, hours=3)
print(d3)

"""
methods associated with timedelta

I can access attributes of timedelta using the dot operator.
"""

td = timedelta(days=2, hours=3)
# Returns the total number of seconds represented by the timedelta object.
total_seconds = td.total_seconds()
print(total_seconds)  # Output: 183600.0

