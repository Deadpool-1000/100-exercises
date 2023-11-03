#  Todays date in formatted Today is {day}, {Month} {date}, {year}
import calendar
from datetime import datetime
today: datetime = datetime.now()
day_of_week = {
    0: "Monday",
    1: "Tuesday"
}


print(f'Today is {calendar.day_name[today.weekday()]}, {calendar.month_name[today.month]} {today.day}, {today.year}')