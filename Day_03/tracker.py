# Personal Expense Tracker

class Expense:

    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def display(self):
        print("---------------------------")
        print(f"Expense : {self.name}")
        print(f"Category: {self.category}")
        print(f"Amount  : ₹{self.amount}")


# List to store all expenses
expenses = []

while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":

        name = input("Enter Expense Name: ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: ₹"))

        expense = Expense(name, category, amount)
        expenses.append(expense)

        print("✅ Expense Added Successfully!")

    # View Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found!")

        else:
            print("\n------ YOUR EXPENSES ------")

            for expense in expenses:
                expense.display()

    # Show Total Expense
    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense.amount

        print(f"\n💰 Total Expense = ₹{total}")

    # Exit
    elif choice == "4":

        print("Thank you for using Personal Expense Tracker!")
        break

    # Invalid Choice
    else:

        print("❌ Invalid choice! Please try again.")