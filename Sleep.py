Sleep_Time= int(input("Enter you sleep time in hours "))
if Sleep_Time >= 9:
    print("You may have Over Slept")
elif 5 <= Sleep_Time < 9:
    print("You have Enough Sleep")
else:
    print("You need more Sleep")