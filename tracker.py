# Project:      Expense Tracker (Installment 4: The Tracker Makes Decisions)
# Author:       Daniel Ezra C. Galopo
# Description:  Categorizes expense size, warning on large purchases, and provides budget verdicts.

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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense. ")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense. ")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

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

if over_budget:
    print(f"Over budget by\t${total - budget}!")
elif total > (0.9 * budget):
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. \t${left} left.")

# Footer
print ("-" * 40)
print ("Made by: Daniel Ezra C. Galopo | Installment 4")
print ("=" * 40)



