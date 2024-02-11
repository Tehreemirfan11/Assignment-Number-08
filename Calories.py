age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
activity= input("Enter your activity level (Less Active, More Active, Moderate): ")

if activity == "Less Active":
    calorie = 1.2 * (655 + (9.6 * weight) + (1.8 * age))
elif activity == "Moderate":
    calorie = 1.55 * (655 + (9.6 * weight) + (1.8 * age))
elif activity == "More Active":
    calorie = 1.9 * (655 + (9.6 * weight) + (1.8 * age))
else:
    print("Invalid Activity Level")
print(f"Your calorie goal is {calorie}")   