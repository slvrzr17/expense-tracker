# Project:      Expense Tracker (Installment 2: Talking to the User)
# Author:       Daniel Ezra C. Galopo
# Description:  Asks the user for their name, logs two expenses, and calculates total and average expense

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

item1 = input("First Expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second Expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print ("")
print ("-" * 40)
print ("SUMMARY")
print (f"  - {item1}:\t${amount1}")
print (f"  - {item2}:\t${amount2}")
print (f"Total spent:\t${total}")
print (f"Average:\t${average}")

# Footer
print ("-" * 40)
print ("Made by: Daniel Ezra C. Galopo | Installment 2")
print ("=" * 40)