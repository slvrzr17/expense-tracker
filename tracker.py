# Project:      Expense Tracker (Installment 5: The Menu Comes Alive)
# Author:       Daniel Ezra C. Galopo
# Description:  Interactive menu loop that logs expenses, keeps a running count and subtotal, displays totals, and exits.

print ("=" * 40)
print ("\tEXPENSE TRACKER\n\tKnow where your money goes.")
print ("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print (f"Welcome, {name}!")

subtotal = 0
count = 0

while True:
    print ("\nMAIN MENU")
    print ("  [1] Add an expense")
    print ("  [2] View all expenses\t\t(coming soon)")
    print ("  [3] Show total spent")
    print ("  [4] Exit\n")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print ("  Huge expense - are you sure?")
        elif amount > 100:
            print ("  Big expense. ")
        elif amount > 50:
            print ("  Moderate expense.")
        else:
            print ("  Small expense.")

    elif choice == "2":
        print ("  Coming soon: the tracker can't remember each item yet")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        print (f"  Expenses:\t{count}")
        print (f"  Subtotal:\t${subtotal}")
        print (f"  Tax ({tax_percent}%):\t${tax}")
        print (f"  Grand Total:\t${total}")
        if over_budget:
            print(f"  Over budget by\t${total - budget}!")
        elif total > (0.9 * budget):
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. \t${left} left.")

    elif choice == "4":
        # Footer
        print (f"Goodbye, {name}!")
        print ("-" * 40)
        print ("Made by: Daniel Ezra C. Galopo | Installment 5")
        print ("=" * 40)
        break

    else:
        print ("  Please choose 1, 2, 3, or 4.")