lunch = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groce = float(input("How much money do you spend on groceries in a week?"))

weekly = lunch*price+groce
daily = weekly/7
print("Average food expenditure:")
print("Daily:",daily,"euros")
print("Weekly:",weekly,"euros")