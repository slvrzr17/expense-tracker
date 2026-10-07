# Project:      Expense Tracker (Installment 3: The Tracker Does Math)
# Author:       Daniel Ezra C. Galopo
# Description:  Calculates tax, grand total, if expense exceeds budget, and if there is anything left from the budget

print ("=" * 40)
print ("\tEXPENSE TRACKER\n\tKnow where your money goes.")
print ("=" * 40)

print ("MAIN MENU")
print ("  [1] Add an expense\t\t(coming soon)")
print ("  [2] View all expenses\t\t(coming soon)")
print ("  [3] Show total spent\t\t(coming soon)")
print ("  [4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print (f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0

item1 = input("First Expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print ("")
print ("-" * 40)
print ("SUMMARY")
print (f"  - {item1}:\t${amount1}")
print (f"  - {item2}:\t${amount2}")
print (f"Subtotal:\t${subtotal}")
print (f"Average:\t${average}")
print (f"Tax ({tax_percent}%):\t${tax}")
print (f"Grand Total:\t${total}")
print (f"Over budget?\t{over_budget}")
print (f"Left in budget:\t${left}")

# Footer
print ("-" * 40)
print ("Made by: Daniel Ezra C. Galopo | Installment 3")
print ("=" * 40)