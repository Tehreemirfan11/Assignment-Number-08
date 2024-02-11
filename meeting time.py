Meeting1 = ["9:00 AM", "2:30 PM", "2:00 PM", "4:00 PM"]
Meeting2 = ["9:30 AM", "2:30 PM", "3:00 PM", "4:30 PM"]
Meeting3= ["9:00 AM", "2:30 PM", "2:30 PM", "4:00 PM"]

common = set(Meeting1) & set(Meeting2) & set(Meeting3)

if common:
    print("Common meeting times:")
    for slot in common:
        print(slot)
else:
    print("No common meeting times found.")