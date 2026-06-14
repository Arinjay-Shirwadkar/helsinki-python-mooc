print("Please type in integer numbers. Type in 0 to finish.")
Sum = 0
c=0
p=0
ne=0

while True:
    n = int(input("Number:"))
    if n==0:
        break
    elif n>0:
        p+=1
    else:
        ne+=1
    c+=1
    Sum+=n

print("Numbers typed in",c)
print("The sum of the numbers is",Sum)
print("The mean of the numbers is",(float(Sum)/c))
print('Positive numbers',p)
print('Negative numbers',ne)
