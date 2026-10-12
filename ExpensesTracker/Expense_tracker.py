#========================================================
# Expense Tracker
# Langauge : Python
#========================================================
expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
# split is used to split while 1 shows that if already a value contians more,
#  like phone-case-100 soo it will deal with it 
            # rsplit is used to split from right side
            # split is used to split from left side
            item, amount = line.strip().split("-", 1)
            expenses.append((item, float(amount)))
except FileNotFoundError:
    pass

print("======== Expense Tracker ========")
print("Welcome to the Expense Tracker!")
print("You can track your expenses and view your spending habits.")
print("Let's get started!")
print("=================================")
while True:  
    print("\nPlease select an option:")  
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Clear Expenses")
    choice = input("Enter your choice: ")

    if choice == "1":
        items = input("Enter the item name: ")
        try:
            amount = float(input("Enter the amount spent: "))
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid amount.")
                continue
            expenses.append((items, amount))

            with open("expenses.txt", "a") as file:
                file.write(f"{items}-{amount}\n")
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.") 

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
          print("======== Your Expenses ========")
          for item, amount in expenses:
            # 2f is used to round off decimal to 2 decimal places 
            print(f"{item}: ${amount:.2f}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
           total = sum(amount for _, amount in expenses)
           print(f"=====Total Expenses=========")
           print(f"${total:.2f}")

    elif choice == "4":
            expenses.clear()
            print("All expenses cleared.")
            with open("expenses.txt", "w") as file:
              file.write("")

    else:
            print("Invalid choice. Please try again.")
