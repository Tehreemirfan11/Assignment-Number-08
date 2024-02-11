price = int(input("Price of the item: "))
quantity = int(input("quantity of item: "))
total_cost = price * quantity
if total_cost > 1000:
    Total= total_cost * 0.1
    discount= total_cost - Total
    print(f"Your discount is {discount}")
    print(f"Your Total Cost is {Total}")
else:
    print("No Discount")   
    print(f"Your Total Cost is {total_cost}")