n = int(input("Value of gift:"))
tax=0.0
if n<5000:
    print("No tax!")
elif n<25000:
    tax = (100+(n-5000)*0.08)
elif n<55000:
    tax = (1700+(n-25000)*0.1)
elif n<200000:
    tax = (4700+(n-55000)*0.12)
elif n<1000000:
    tax = (22100+(n-200000)*0.15)
else:
    tax = (142100+(n-1000000)*0.17)

if tax!=0:
    print("Amount of tax:",tax,"euros")