year = int(input("Enter year: "))
month = int(input("Enter Month: "))

if 1 <= month <= 12:
    leap =(year % 400 == 0)
    days= 0
    if month == 2:
        days = 29 if leap else 28
    elif month in {4, 6, 9, 11}:
        days = 30
    else:
        days = 31
    print(f"The number of days in {month}th month of {year} is: {days}")
else:
    print("Wrong Month.")