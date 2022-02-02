# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = int(input("enter a year: "))  # year
mm = int(input("enter a month: "))    # month

print(calendar.month(yy, mm))     # display the calendar