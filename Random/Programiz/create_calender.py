# create a plain text calender

import calendar
text_calendar = calendar.TextCalendar(calendar.SUNDAY)
format_calendar = text_calendar.formatmonth(2021, 1)
format_calendar_year = text_calendar.formatyear(2020)
print(format_calendar)
print(format_calendar_year)