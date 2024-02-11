Year = int(input("Write a Year: "))
if (Year % 4 == 0 and Year % 100 != 0):
    print((f"{Year} is a leap year."))
elif (Year % 400 == 0):
    print(f"{Year} is leap year.")
else:
    print(f"{Year} is not a leap year.")