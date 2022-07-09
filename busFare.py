# Checking the day of the week and printing the bus fare for that day.
from datetime import date
import calendar

current_date = date.today()
current_day = calendar.day_name[current_date.weekday()]
stripped_day = current_day[0:3]

if stripped_day == 'Sat':
    print("Bus fare is: 60")
elif stripped_day == 'Sun':
    print("Bus fare is: 80")
else:
    print("Bus fare is: 100")
