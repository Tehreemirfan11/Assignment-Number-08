weight = float(input("Enter your weight in kilograms: "))
exercise= input("Exercise = (light, moderate, intense): ")
light= 20
moderate= 30
intense= 50
if exercise == "light":
    water = light * weight
elif exercise == "moderate":
    water = moderate* weight
elif exercise == "intense":
    water = intense* weight
else:
    print("Please Enter Write Information") 

print(f"To stay hydrated, you should drink {water} milliliters of water per day.")