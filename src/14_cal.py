"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#the sys module can access the arguments passed into the cmd prompt
# slice it because the first argv is always the file itself
month_and_year = sys.argv[1:]

calendar_to_print = calendar.TextCalendar()

# print(month_and_year)
#check the length of the args list
if len(month_and_year) > 1:
    # if more than 1 then assign the first index as the month and the last as the year
    month = int(month_and_year[0])
    year = int(month_and_year[1])
    # and then print out the calendar using your month and year
    calendar_to_print.prmonth(year, month)
# otherwise
else:
    # grab today's month and year for calendar
    modern_month_and_year = datetime.today().strftime('%m-%y').split("-")
    #and then assign those variables to it
    month = int(modern_month_and_year[0])
    year = int(modern_month_and_year[1])
    # and then print out the calendar using your month and year
    calendar_to_print.prmonth(year, month)



