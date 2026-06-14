y = int(input("Enter a year"))

if y%4==0:
    if y%100==0:
        if y%400==0:
            b=True
        else: b=False
    else: b=True
else : b=False

if b:
    print("That year is a leap year.")
else : 
    print("That year is not a leap year")
