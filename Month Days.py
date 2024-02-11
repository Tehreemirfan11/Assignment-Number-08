Month = int(input("Enter month a between 1 to 12: "))
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= Month <= 12:
    print(f"{Month}th month has {days[Month]} days.")
else:
    print("Wrong Month")