import calendar

year = int(input("please enter the year: "))
month = int(input("please enter the month: "))

calendar_view = calendar.month(year,month)

print(f"The calender for the year {year} is: ")
print()
print(calendar_view)