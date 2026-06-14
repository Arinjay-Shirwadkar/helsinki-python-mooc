hw = float(input("Hourly wage:"))
h = float(input("Hours worked:"))
d = input("Day of the week:")
if d=="Sunday":
    h*=2
print("Daily wages:",(hw*h),"euros")