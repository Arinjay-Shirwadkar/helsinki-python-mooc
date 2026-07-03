from datetime import datetime, timedelta



name = input("Filename: ")
dat = input("Starting date: ")
s = dat.split('.')
date = datetime(int(s[2]),int(s[1]),int(s[0]))
#date = datetime.strptime(dat,"%d.%m.%y")
num= input("How many days: ")
print("Please type in screen time in minutes on each day (TV computer mobile):")


with open(name,'w') as file:
        for i in range(0,int(num)):
            #to hell with these crackpot methods. Why not explain classes first?
    
            file.write(input(f"Screen time {date.day}.{date.month}.{date.year}: ")+'\n')
            date = date + timedelta(days=1)
        print("Data stored in file",name)