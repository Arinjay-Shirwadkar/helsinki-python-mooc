from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
millenium = datetime(2000,1,1)
diff = millenium - datetime(year , month , day+1)  #timedelta obj

if diff.days<=0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {diff.days} days old on the eve of the new millennium.") 