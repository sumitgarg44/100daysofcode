# Header
print(f"\nWelcome to the Tip calculator!")

# Inputs and variables
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate and print bill
bill_with_tip = bill * (1 + tip / 100)
bill_per_person = bill_with_tip / people
print(f"\nEach person should pay: ${round(bill_per_person,2)}")
