o = int(input("Enter a year"))
y=o+1

while True:
    if y%4==0:
        if y%100==0 and y%400!=0:
            y=y+1
            continue
        else: 
            leap = y
            break
    else:
        y=y+1
        continue

print(f"The next leap year after {o} is {leap}")