# Program to display calendar of the given month and year
# calender module:  https://docs.python.org/3/library/calendar.html

import calendar

yy = int(input())
mm = int(input())
print(calendar.month(yy, mm))
print(calendar.isleap(yy))
