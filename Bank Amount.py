Pin = "0485"
Balance = 1000
user = input("Enter Your Pin: ")
if user == Pin:
    withdrawal_amount = float(input("Enter Withdrawal Amount: "))
    if withdrawal_amount <= Balance:
        Balance -= withdrawal_amount
        print(f"Withdrawal successful! your Remaining Amount is : {Balance} Rupees")
    else:
        print(f"You have not {user} Rupees")
else:
    print("Incorrect PIN")